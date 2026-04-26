# kmr_chains_operations_func.py
"""
KMR Chains - Functional Operations Extension (Version 2)
Version: 1.0.1
License: GPL 3.0
Author: Sergei Terikhov
Description: Extends KMR chains to support functional values and compositions
"""

from typing import Any, Callable, Dict
import inspect
import sympy as sp


class FunctionRegistry:
    """Registry for function definitions and operations"""

    # Predefined basic functions
    BASIC_FUNCTIONS = {
        'identity': lambda x: x,
        'square': lambda x: x ** 2,
        'cube': lambda x: x ** 3,
        'reciprocal': lambda x: 1 / x,
        'sqrt': lambda x: x ** 0.5,
        'exp': lambda x: sp.exp(x) if hasattr(sp, 'exp') else __import__('math').exp(x),
        'ln': lambda x: sp.log(x) if hasattr(sp, 'log') else __import__('math').log(x),
        'log': lambda x: sp.log(x) if hasattr(sp, 'log') else __import__('math').log(x),
        'sin': lambda x: sp.sin(x) if hasattr(sp, 'sin') else __import__('math').sin(x),
        'cos': lambda x: sp.cos(x) if hasattr(sp, 'cos') else __import__('math').cos(x),
        'tan': lambda x: sp.tan(x) if hasattr(sp, 'tan') else __import__('math').tan(x),
        'kmr_direct': lambda x, k: x / (1 + k * x),
        'kmr_inverse': lambda x, k: x / (1 - k * x),
    }

    @staticmethod
    def create_function(expr: str, var_name: str = 'x') -> Callable:
        """
        Create a function from string expression

        Args:
            expr: Mathematical expression as string
            var_name: Variable name

        Returns:
            Callable function
        """
        try:
            # Try using sympy for symbolic expressions
            var = sp.symbols(var_name)
            sympy_expr = sp.sympify(expr)
            return sp.lambdify(var, sympy_expr, 'numpy')
        except:
            # Fallback to eval (use with caution!)
            # Note: In production code, you should implement safer parsing
            return lambda x: eval(expr, {'x': x, 'math': __import__('math')})

    @staticmethod
    def compose(f: Callable, g: Callable) -> Callable:
        """
        Compose two functions: f ∘ g

        Args:
            f: Outer function
            g: Inner function

        Returns:
            Composed function f(g(x))
        """

        def composed(*args, **kwargs):
            return f(g(*args, **kwargs))

        return composed

    @staticmethod
    def partial_apply(f: Callable, *args, **kwargs) -> Callable:
        """
        Partially apply arguments to a function

        Args:
            f: Function to partially apply

        Returns:
            Partially applied function
        """
        return lambda *remaining_args, **remaining_kwargs: \
            f(*args, *remaining_args, **{**kwargs, **remaining_kwargs})


class FunctionalOperationHandlers:
    """Handlers for operations with functional values"""

    def __init__(self, space_getter: Callable):
        """
        Args:
            space_getter: Function that returns KMRChainSpace instance
        """
        self.get_space = space_getter
        self.registry = FunctionRegistry()

    def _resolve_value(self, value: Any) -> Any:
        """Resolve value - could be an ID or direct value"""
        space = self.get_space()

        # If it's a string ID (32 chars), try to get from space
        if isinstance(value, str) and len(value) == 32:
            try:
                return space.get_chain_value(value)
            except (ValueError, KeyError):
                pass

        return value

    def _ensure_function(self, value: Any) -> Callable:
        """Convert value to function if needed"""
        # First resolve possible ID
        resolved = self._resolve_value(value)

        if callable(resolved):
            return resolved
        elif isinstance(resolved, str):
            # Check if it's a predefined function name
            if resolved in self.registry.BASIC_FUNCTIONS:
                return self.registry.BASIC_FUNCTIONS[resolved]
            # Try to parse as expression
            try:
                return self.registry.create_function(resolved)
            except:
                # Return constant function
                try:
                    constant = float(resolved)
                    return lambda x: constant
                except:
                    return lambda x: resolved
        else:
            # Return constant function
            try:
                constant = float(resolved)
                return lambda x: constant
            except:
                return lambda x: resolved

    def _apply_to_function(self, f: Callable, operation: str, param: Any) -> Callable:
        """Apply operation to a function"""
        param_func = self._ensure_function(param)

        if operation == '⊙':
            # f(x) ⊙ g(x) = f(x) / (1 + f(x) * g(x))
            return lambda x: f(x) / (1 + f(x) * param_func(x))
        elif operation == '⊘':
            # f(x) ⊘ g(x) = f(x) / (1 - f(x) * g(x))
            return lambda x: f(x) / (1 - f(x) * param_func(x))
        elif operation == '+':
            # f(x) + g(x)
            return lambda x: f(x) + param_func(x)
        elif operation == '-':
            # f(x) - g(x)
            return lambda x: f(x) - param_func(x)
        elif operation == '*':
            # f(x) * g(x)
            return lambda x: f(x) * param_func(x)
        elif operation == '/':
            # f(x) / g(x)
            return lambda x: f(x) / param_func(x)
        elif operation == '∘':
            # Function composition: f ∘ g
            return self.registry.compose(f, param_func)
        else:
            raise ValueError(f"Unknown operation for functions: {operation}")

    # Basic function creation
    def make_function(self, a: Any, b: Any) -> Callable:
        """
        Create a function from parameter b

        Args:
            a: Ignored (chain value before)
            b: Function definition (callable, string, or constant)

        Returns:
            Callable function
        """
        return self._ensure_function(b)

    # KMR operations with functions
    def kmr_direct_func(self, a: Any, b: Any) -> Any:
        """Direct KMR operation with functional support"""
        a_func = self._ensure_function(a)
        return self._apply_to_function(a_func, '⊙', b)

    def kmr_inverse_func(self, a: Any, b: Any) -> Any:
        """Inverse KMR operation with functional support"""
        a_func = self._ensure_function(a)
        return self._apply_to_function(a_func, '⊘', b)

    # Arithmetic operations with functions
    def add_func(self, a: Any, b: Any) -> Any:
        """Addition with functional support"""
        a_func = self._ensure_function(a)
        return self._apply_to_function(a_func, '+', b)

    def sub_func(self, a: Any, b: Any) -> Any:
        """Subtraction with functional support"""
        a_func = self._ensure_function(a)
        return self._apply_to_function(a_func, '-', b)

    def mul_func(self, a: Any, b: Any) -> Any:
        """Multiplication with functional support"""
        a_func = self._ensure_function(a)
        return self._apply_to_function(a_func, '*', b)

    def div_func(self, a: Any, b: Any) -> Any:
        """Division with functional support"""
        a_func = self._ensure_function(a)
        return self._apply_to_function(a_func, '/', b)

    def compose_func(self, a: Any, b: Any) -> Any:
        """Function composition"""
        a_func = self._ensure_function(a)
        b_func = self._ensure_function(b)
        return self.registry.compose(a_func, b_func)

    def partial_apply_func(self, a: Any, b: Any) -> Any:
        """Partial application of function"""
        a_func = self._ensure_function(a)
        return self.registry.partial_apply(a_func, b)


def create_functional_handlers(space_getter: Callable):
    """Create functional operation handlers for a specific space"""
    handlers = FunctionalOperationHandlers(space_getter)

    return {
        # Function creation
        'make_func': handlers.make_function,

        # KMR operations
        '⊙f': handlers.kmr_direct_func,
        '⊘f': handlers.kmr_inverse_func,

        # Arithmetic operations
        '+f': handlers.add_func,
        '-f': handlers.sub_func,
        '*f': handlers.mul_func,
        '/f': handlers.div_func,

        # Function-specific operations
        '∘': handlers.compose_func,
        'partial': handlers.partial_apply_func,
    }


# Function operation aliases
FUNCTION_OPERATION_ALIASES = {
    # Function creation
    'identity': 'make_func',
    'create_func': 'make_func',
    'func': 'make_func',

    # KMR operations
    'dircly_f': '⊙f',
    'direct_f': '⊙f',
    'kmr_direct_f': '⊙f',

    'invly_f': '⊘f',
    'inverse_f': '⊘f',
    'kmr_inverse_f': '⊘f',

    # Arithmetic operations
    'add_f': '+f',
    'addition_f': '+f',
    'plus_f': '+f',

    'sub_f': '-f',
    'subtract_f': '-f',
    'minus_f': '-f',

    'mul_f': '*f',
    'multiply_f': '*f',
    'times_f': '*f',

    'div_f': '/f',
    'divide_f': '/f',
    'division_f': '/f',

    # Function-specific operations
    'compose': '∘',
    'composition': '∘',
    'partial_apply': 'partial',
}


# Helper functions for working with functional chains
def evaluate_function_chain(element_id: str, space, *args, **kwargs) -> Any:
    """Evaluate functional chain at given arguments"""
    func = space.get_chain_value(element_id)
    if callable(func):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Try with single argument
            if len(args) == 1:
                return func(args[0])
            else:
                raise e
    else:
        return func


def create_kmr_function(k_value, base_func=None):
    """
    Create a KMR-transformed function

    Args:
        k_value: K parameter for KMR transform
        base_func: Base function (default: identity)

    Returns:
        Function f(x) = base_func(x) ⊙ k_value
    """
    if base_func is None:
        base_func = lambda x: x

    def kmr_func(x):
        base_val = base_func(x)
        return base_val / (1 + base_val * k_value)

    return kmr_func


def create_chain_function(element_id: str, space):
    """
    Create a function from a chain

    Args:
        element_id: ID of the chain element
        space: KMRChainSpace instance

    Returns:
        Function representing the entire chain
    """

    def chain_func(*args, **kwargs):
        value = space.get_chain_value(element_id)
        if callable(value):
            return value(*args, **kwargs)
        else:
            return value

    return chain_func