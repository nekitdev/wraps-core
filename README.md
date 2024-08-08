# `wraps-core`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Core functionality of wraps.*

## Installing

**Python 3.8 or above is required.**

### `pip`

Installing the library with `pip` is quite simple:

```console
$ pip install wraps-core
```

Alternatively, the library can be installed from the source:

```console
$ pip install git+https://github.com/nekitdev/wraps-core.git
```

Or via cloning the repository:

```console
$ git clone https://github.com/nekitdev/wraps-core.git
$ cd wraps-core
$ pip install .
```

### `uv`

You can add `wraps-core` as a dependency with the following command:

```console
$ uv add wraps-core
```

## Examples

### Option

[`Option[T]`][wraps_core.option.Option] type represents an optional value: every option is either
[`Some[T]`][wraps_core.option.Some] and contains a value, or [`Null`][wraps_core.option.Null],
and does not.

Here is an example of `divide` function returning `Option[float]` instead of raising an error when
the denominator is zero:

```python
# option.py

from wraps_core import NULL, Option, Some


def divide(numerator: float, denominator: float) -> Option[float]:
    return Some(numerator / denominator) if denominator else NULL
```

There are two ways to process the resulting option: either via pattern matching or predicates.

```python
# option_matching.py

from wraps_core import Null, Some

from option import divide

DIVISION_BY_ZERO = "division by zero"

match divide(1.0, 2.0):
    case Some(value):
        print(value)

    case Null():
        print(DIVISION_BY_ZERO)
```

```python
# option_predicates.py

from option import divide

DIVISION_BY_ZERO = "division by zero"

option = divide(1.0, 2.0)

if option.is_some():
    # here we know that the `option` is `Some[float]`, so it is safe to unwrap it
    print(option.unwrap())

else:
    # and here we know that the `option` is `Null`
    print(DIVISION_BY_ZERO)
```

Note that both examples are fully type safe.

### Result

[`Result[T, E]`][wraps_core.result.Result] is the type used for returning and propagating errors.
It has two variants, [`Ok[T]`][wraps_core.result.Ok], representing success and containing a value,
and [`Error[E]`][wraps_core.result.Error], representing error and containing an error value.

Below is the enhanced `divide` function from above, now using `Result[float, DivideError]`
instead of `Option[float]`.

```python
# result.py

from enum import Enum

from wraps_core import Error, Ok, Result


class DivideError(Enum):
    DIVISION_BY_ZERO = "division by zero"


def divide(numerator: float, denominator: float) -> Result[float, DivideError]:
    return Ok(numerator / denominator) if denominator else Error(DivideError.DIVISION_BY_ZERO)
```

Using new `divide` is as simple as the old one:

```python
# result_matching.py

from wraps_core import Error, Ok

from result import divide

match divide(1.0, 2.0):
    case Ok(value):
        print(value)

    case Error(error):
        print(error.value)  # we use `value` here to get error details
```

```python
# result_predicates.py

from result import divide

result = divide(1.0, 2.0)

if result.is_ok():
    # here we know the `result` is `Ok[float]`, so we can unwrap it safely
    print(result.unwrap())

else:
    # and here the `result` is `Error[DivideError]`, so we can unwrap the error safely
    print(result.unwrap_error().value)
```

### Decorators

### Early Return

Early return functionality (like the *question mark* (`?`) operator in Rust) is implemented via
`early` methods (for both [`Option[T]`][wraps_core.option.Option]
and [`Result[T, E]`][wraps_core.result.Result] types) combined with the
[`@early_option`][wraps_core.early.decorators.early_option] and
[`@early_result`][wraps_core.early.decorators.early_result] decorators respectively.

Here is an example using [`wrap_option_on`][wraps_core.option.wrap_option_on] to catch errors:

```python
from wraps_core import Option, early_option, wrap_option_on


@wrap_option_on(ValueError)
def parse(string: str) -> float:
    return float(string)


@wrap_option_on(ZeroDivisionError)
def divide(numerator: float, denominator: float) -> float:
    return numerator / denominator


@early_option
def divide_string(x: str, y: str) -> Option[float]:
    return divide(parse(x).early(), parse(y).early())
```

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send us an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `wraps-core` [here][Security].

## Contributing

If you are interested in contributing to `wraps-core`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`wraps-core` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/chat

[Actions]: https://github.com/nekitdev/wraps-core/actions

[Changelog]: https://github.com/nekitdev/wraps-core/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/wraps-core/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/wraps-core/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/wraps-core/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/wraps-core/blob/main/LICENSE

[Package]: https://pypi.org/project/wraps-core
[Coverage]: https://codecov.io/gh/nekitdev/wraps-core
[Documentation]: https://nekitdev.github.io/wraps-core

[Discord Badge]: https://img.shields.io/discord/728012506899021874
[License Badge]: https://img.shields.io/pypi/l/wraps-core
[Version Badge]: https://img.shields.io/pypi/v/wraps-core
[Downloads Badge]: https://img.shields.io/pypi/dm/wraps-core

[Documentation Badge]: https://github.com/nekitdev/wraps-core/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/wraps-core/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/wraps-core/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/wraps-core/branch/main/graph/badge.svg

[wraps-decorators]: https://github.com/nekitdev/wraps-decorators

[wraps_core.option.Option]: https://nekitdev.github.io/wraps-core/reference/option#wraps_core.option.Option
[wraps_core.option.Some]: https://nekitdev.github.io/wraps-core/reference/option#wraps_core.option.Some
[wraps_core.option.Null]: https://nekitdev.github.io/wraps-core/reference/option#wraps_core.option.Null

[wraps_core.option.wrap_option_on]: https://nekitdev.github.io/wraps-core/reference/option#wraps_core.option.wrap_option_on

[wraps_core.result.Result]: https://nekitdev.github.io/wraps-core/reference/result#wraps_core.result.Result
[wraps_core.result.Ok]: https://nekitdev.github.io/wraps-core/reference/result#wraps_core.result.Ok
[wraps_core.result.Error]: https://nekitdev.github.io/wraps-core/reference/result#wraps_core.result.Error

[wraps_core.early.decorators.early_option]: https://nekitdev.github.io/wraps-core/reference/early/decorators#wraps_core.early.decorators.early_option
[wraps_core.early.decorators.early_result]: https://nekitdev.github.io/wraps-core/reference/early/decorators#wraps_core.early.decorators.early_result
