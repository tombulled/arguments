from arguments import Arguments
import pytest


@pytest.fixture
def arguments() -> Arguments:
    return Arguments("foo", "bar", sep=", ")


def test_args(arguments: Arguments) -> None:
    assert arguments.args == ("foo", "bar")


def test_kwargs(arguments: Arguments) -> None:
    assert arguments.kwargs == {"sep": ", "}


def test_len(arguments: Arguments) -> None:
    assert len(arguments) == 3


def test_iter(arguments: Arguments) -> None:
    assert tuple(arguments) == ("foo", "bar", ", ")


def test_getitem(arguments: Arguments) -> None:
    assert arguments[0] == "foo"
    assert arguments[1] == "bar"
    assert arguments[2] == ", "

    with pytest.raises(IndexError):
        arguments[3]


def test_call(arguments: Arguments) -> None:
    def consumer(*args, **kwargs) -> None:
        assert arguments.args == args
        assert arguments.kwargs == kwargs

    arguments(consumer)
