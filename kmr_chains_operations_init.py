"""
KMR Extensions - Convenience functions for extended operations
Version: 1.0.0
License: GPL 3.0
"""

from kmr_chains import get_default_space
from kmr_chains_operations_by_id import create_id_handlers, ID_OPERATION_ALIASES


def initialize_id_operations(space=None):
    """Initialize ID operations for a space"""
    if space is None:
        space = get_default_space()

    id_handlers = create_id_handlers(lambda: space)

    for op_symbol, handler in id_handlers.items():
        space.register_