# kmr_chains.py
"""
KMR Chains - Abstract Minimal Chain Implementation
Version: 5.5.5
License: GPL 3.0 (see LICENSE)
Author: Sergei Terikhov
"""

import hashlib
import secrets
from typing import Any, Dict
from kmr_operations import kmr_dircly, kmr_invly


class PublicChainElement:
    """Public part of chain element"""

    def __init__(self, element_id: str, value: Any, operation: str):
        self.id = element_id
        self.value = value
        self.operation = operation

    def to_dict(self) -> dict:
        return {'id': self.id, 'value': self.value, 'operation': self.operation}


class PrivateChainElement:
    """Private part of chain element"""

    def __init__(self, element_id: str, parent_id: str,
                 chain_value_before: Any, chain_value_after: Any):
        self.id = element_id
        self.parent_id = parent_id
        self.chain_value_before = chain_value_before
        self.chain_value_after = chain_value_after

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'parent_id': self.parent_id,
            'chain_value_before': self.chain_value_before,
            'chain_value_after': self.chain_value_after
        }


class KMRChainSpace:
    """KMR Chain Space with abstract minimal design"""

    def __init__(self):
        self.public_heap: dict[str, PublicChainElement] = {}
        self.private_heap: dict[str, PrivateChainElement] = {}
        self._operation_handlers = {}
        self._operation_aliases = {}
        self._register_default_handlers()

    def _register_default_handlers(self):
        """Register default operation handlers"""
        # For numeric types, use kmr_operations functions
        self.register_operation('⊙', kmr_dircly, {'dircly': '⊙', 'direct': '⊙', 'dir': '⊙'})
        self.register_operation('⊘', kmr_invly, {'invly': '⊘', 'inverse': '⊘', 'inv': '⊘'})

        # Basic arithmetic operations
        self.register_operation('+', lambda a, b: a + b, {'add': '+'})
        self.register_operation('-', lambda a, b: a - b, {'sub': '-'})
        self.register_operation('*', lambda a, b: a * b, {'mul': '*'})
        self.register_operation('/', lambda a, b: a / b, {'div': '/'})

    def register_operation(self, op_symbol: str, handler, op_map: Dict = None):
        """Register custom operation handler for any object type"""
        self._operation_handlers[op_symbol] = handler

        if op_map:
            for alias, target_op in op_map.items():
                self._operation_aliases[alias.lower()] = target_op

    def _apply_operation(self, value_before: Any, operation: str, parameter: Any) -> Any:
        """Apply operation to value - returns result or raises exception"""
        if operation not in self._operation_handlers:
            raise ValueError(f"Unknown operation: {operation}")

        handler = self._operation_handlers[operation]
        try:
            return handler(value_before, parameter)
        except Exception as e:
            raise ValueError(f"Operation {operation} failed: {str(e)}")

    def _generate_id(self) -> str:
        """Generate unique ID"""
        return hashlib.sha256(secrets.token_bytes(32)).hexdigest()[:32]

    def _get_chain_value_before(self, parent_id: str, explicit_value: Any = None) -> Any:
        """Calculate chain_value_before based on parent"""
        if explicit_value is not None:
            return explicit_value

        if parent_id in self.private_heap:
            return self.private_heap[parent_id].chain_value_after

        # Default value when no parent exists
        return 1.0

    def add_element(self,
                    operation: str,
                    value: Any,
                    parent_id: str = None,
                    element_id: str = None,
                    chain_value_before: Any = None) -> str:
        """
        Add element to chain

        Returns:
            Created element ID
        """
        # Operation normalization
        op_map = {
            'dircly': '⊙', 'direct': '⊙', 'dir': '⊙',
            'invly': '⊘', 'inverse': '⊘', 'inv': '⊘',
            'add': '+', 'sub': '-', 'mul': '*', 'div': '/'
        }
        op = operation
        if operation.lower() in self._operation_aliases:
            op = self._operation_aliases[operation.lower()]

        # Generate IDs
        if element_id is None:
            element_id = self._generate_id()
        elif element_id in self.public_heap:
            raise ValueError(f"Element {element_id[:16]}... already exists")

        if parent_id is None:
            parent_id = self._generate_id()

        # Calculate chain values
        before_value = self._get_chain_value_before(parent_id, chain_value_before)
        after_value = self._apply_operation(before_value, op, value)

        # Create and store elements
        public_elem = PublicChainElement(element_id, value, op)
        private_elem = PrivateChainElement(element_id, parent_id, before_value, after_value)

        self.public_heap[element_id] = public_elem
        self.private_heap[element_id] = private_elem

        return element_id

    def check_consistency(self, element_id: str) -> bool:
        """Check if element is consistent with its parent"""
        if element_id not in self.private_heap:
            return False

        element = self.private_heap[element_id]
        parent_id = element.parent_id

        # No parent exists - cannot check consistency
        if parent_id not in self.private_heap:
            return False

        parent = self.private_heap[parent_id]

        # Simple equality check for abstract objects
        try:
            return element.chain_value_before == parent.chain_value_after
        except Exception:
            return False

    def get_chain_value(self, element_id: str) -> Any:
        """Get chain value for element"""
        if element_id not in self.private_heap:
            raise ValueError(f"Element {element_id[:16]}... not found")
        return self.private_heap[element_id].chain_value_after

    def get_element(self, element_id: str) -> tuple[PublicChainElement, PrivateChainElement]:
        """Get both public and private parts of element"""
        if element_id not in self.public_heap or element_id not in self.private_heap:
            raise ValueError(f"Element {element_id[:16]}... not found")
        return self.public_heap[element_id], self.private_heap[element_id]

    def clear(self):
        """Clear chain space"""
        self.public_heap.clear()
        self.private_heap.clear()

    def __str__(self) -> str:
        """String representation"""
        return f"KMRChainSpace(elements={len(self.public_heap)})"


# Global default instance
_default_space = KMRChainSpace()


# Minimal interface functions
def get_default_space() -> KMRChainSpace:
    return _default_space


def add_element(operation: str, value: Any, parent_id: str = None,
                element_id: str = None, chain_value_before: Any = None) -> str:
    return _default_space.add_element(operation, value, parent_id, element_id, chain_value_before)


def check_consistency(element_id: str) -> bool:
    return _default_space.check_consistency(element_id)


def get_chain_value(element_id: str) -> Any:
    return _default_space.get_chain_value(element_id)


def get_element(element_id: str) -> tuple[PublicChainElement, PrivateChainElement]:
    return _default_space.get_element(element_id)
