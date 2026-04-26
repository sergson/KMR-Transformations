# kmr_chains_operations_init.py (обновленный)
"""
KMR Extensions - Convenience functions for extended operations
Version: 1.0.1
License: GPL 3.0
"""

from kmr_chains import get_default_space
from kmr_chains_operations_by_id import create_id_handlers, ID_OPERATION_ALIASES
from kmr_chains_operations_func import create_functional_handlers, FUNCTION_OPERATION_ALIASES


def initialize_id_operations(space=None):
    """Initialize ID operations for a space"""
    if space is None:
        space = get_default_space()

    id_handlers = create_id_handlers(lambda: space)

    for op_symbol, handler in id_handlers.items():
        space.register_operation(op_symbol, handler, op_map=ID_OPERATION_ALIASES)

    return space


def initialize_functional_operations(space=None):
    """Initialize functional operations for a space"""
    if space is None:
        space = get_default_space()

    func_handlers = create_functional_handlers(lambda: space)

    for op_symbol, handler in func_handlers.items():
        space.register_operation(op_symbol, handler, op_map=FUNCTION_OPERATION_ALIASES)

    return space


def initialize_all_operations(space=None):
    """Initialize all extended operations (ID and functional)"""
    if space is None:
        space = get_default_space()

    space = initialize_id_operations(space)
    space = initialize_functional_operations(space)

    return space