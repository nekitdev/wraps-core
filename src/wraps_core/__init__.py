"""Core functionality of wraps."""

__description__ = "Core functionality of wraps."
__url__ = "https://github.com/nekitdev/wraps-core"

__title__ = "wraps_core"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "0.2.0"

from wraps_core.early import (
    EarlyOption,
    EarlyResult,
    early_option,
    early_option_await,
    early_result,
    early_result_await,
)
from wraps_core.either import Either, Left, Right, is_left, is_right
from wraps_core.markers import UNREACHABLE, unreachable
from wraps_core.option import (
    NULL,
    Null,
    Option,
    Some,
    WrapOption,
    WrapOptionAwait,
    is_null,
    is_some,
    wrap_option,
    wrap_option_await,
    wrap_option_await_on,
    wrap_option_on,
    wrap_optional,
)
from wraps_core.panics import PANIC, Panic, panic
from wraps_core.result import (
    Error,
    Ok,
    Result,
    WrapResult,
    WrapResultAwait,
    is_error,
    is_ok,
    wrap_result,
    wrap_result_await,
    wrap_result_await_on,
    wrap_result_on,
)

__all__ = (
    # option
    "Option",
    "Some",
    "Null",
    "NULL",
    "is_some",
    "is_null",
    # optional
    "wrap_optional",
    # option decorators
    "WrapOption",
    "WrapOptionAwait",
    "wrap_option_on",
    "wrap_option_await_on",
    "wrap_option",
    "wrap_option_await",
    # result
    "Result",
    "Ok",
    "Error",
    "is_ok",
    "is_error",
    # result decorators
    "WrapResult",
    "WrapResultAwait",
    "wrap_result_on",
    "wrap_result_await_on",
    "wrap_result",
    "wrap_result_await",
    # either
    "Either",
    "Left",
    "Right",
    "is_left",
    "is_right",
    # early decorators
    "early_option",
    "early_option_await",
    "early_result",
    "early_result_await",
    # early errors
    "EarlyOption",
    "EarlyResult",
    # panics
    "PANIC",
    "Panic",
    "panic",
    # markers
    "UNREACHABLE",
    "unreachable",
)
