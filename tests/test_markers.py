from pytest import fail
from wraps_core.markers import UNREACHABLE, unreachable
from wraps_core.panics import Panic

UNREACHABLE_NEVER_RETURNS = "`unreachable` never returns"


def test_unreachable() -> None:
    try:
        unreachable()

    except Panic as error:
        assert error.message == UNREACHABLE

    else:
        fail(UNREACHABLE_NEVER_RETURNS)


MESSAGE = "unreachable code was reached..."


def test_unreachable_message() -> None:
    message = MESSAGE

    try:
        unreachable(message)

    except Panic as error:
        assert error.message == message

    else:
        fail(UNREACHABLE_NEVER_RETURNS)
