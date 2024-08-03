"""Early returns."""

from wraps_core.early.decorators import (
    early_option,
    early_option_await,
    early_result,
    early_result_await,
)
from wraps_core.early.errors import EarlyOption, EarlyResult

__all__ = (
    # decorators
    "early_option",
    "early_option_await",
    "early_result",
    "early_result_await",
    # errors
    "EarlyOption",
    "EarlyResult",
)
