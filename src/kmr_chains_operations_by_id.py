"""
KMR ID Operations - Handlers for operations with element references
Version: 1.0.0
License: GPL 3.0
Author: Sergei Terikhov
"""

from typing import Any, Callable
from kmr_operations import kmr_dircly, kmr_invly


# Basic handlers for ID operations
class IDOperationHandlers:
    """Handlers for operations that take element IDs as parameters"""

    def __init__(self, space_getter: Callable):
        """
        Args:
            space_getter: Function that returns KMRChainSpace instance
        """
        self.get_space = space_getter

    def _resolve_id(self, element_id: Any) -> Any:
        """Resolve element ID to its chain value"""
        space = self.get_space()

        # If it's not a string or doesn't look like an ID, return as is
        if not isinstance(element_id, str) or len(element_id) != 32:
            return element_id

        # Try to get the value from the space
        try:
            return space.get_chain_value(element_id)
        except (ValueError, KeyError):
            # If not found, return as is (could be a regular value)
            return element_id

    def dircly_id(self, a: Any, b: Any) -> Any:
        """Direct KMR operation with ID resolution"""
        resolved_b = self._resolve_id(b)
        return kmr_dircly(a, resolved_b)

    def invly_id(self, a: Any, b: Any) -> Any:
        """Inverse KMR operation with ID resolution"""
        resolved_b = self._resolve_id(b)
        return kmr_invly(a, resolved_b)

    def add_id(self, a: Any, b: Any) -> Any:
        """Addition with ID resolution"""
        resolved_b = self._resolve_id(b)
        return a + resolved_b

    def sub_id(self, a: Any, b: Any) -> Any:
        """Subtraction with ID resolution"""
        resolved_b = self._resolve_id(b)
        return a - resolved_b

    def mul_id(self, a: Any, b: Any) -> Any:
        """Multiplication with ID resolution"""
        resolved_b = self._resolve_id(b)
        return a * resolved_b

    def div_id(self, a: Any, b: Any) -> Any:
        """Division with ID resolution"""
        resolved_b = self._resolve_id(b)
        return a / resolved_b


# Optional: factory for creating handlers
def create_id_handlers(space_getter: Callable):
    """Create ID operation handlers for a specific space"""
    handlers = IDOperationHandlers(space_getter)

    return {
        '⊙id': handlers.dircly_id,
        '⊘id': handlers.invly_id,
        '+id': handlers.add_id,
        '-id': handlers.sub_id,
        '*id': handlers.mul_id,
        '/id': handlers.div_id,
    }


# Optional: dictionary of aliases for ID operations
ID_OPERATION_ALIASES = {
    # Main KMR operations
    'dircly_id': '⊙id',
    'direct_id': '⊙id',
    'dir_id': '⊙id',
    'kmr_direct_id': '⊙id',

    'invly_id': '⊘id',
    'inverse_id': '⊘id',
    'inv_id': '⊘id',
    'kmr_inverse_id': '⊘id',

    # Arithmetic operations
    'add_id': '+id',
    'addition_id': '+id',
    'plus_id': '+id',

    'sub_id': '-id',
    'subtract_id': '-id',
    'minus_id': '-id',

    'mul_id': '*id',
    'multiply_id': '*id',
    'times_id': '*id',

    'div_id': '/id',
    'divide_id': '/id',
    'division_id': '/id',
}