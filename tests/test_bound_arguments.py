from inspect import Signature
from typing import Callable
from arguments import Arguments, BoundArguments
import pytest
import inspect


@pytest.fixture
def function() -> Callable:
    def say(message: str, exclaim: bool = False) -> None:
        ...

    return say

@pytest.fixture
def signature(function: Callable) -> Signature:
    return inspect.signature(function)


@pytest.fixture
def arguments() -> Arguments:
    return Arguments("foo", exclaim=True)


@pytest.fixture
def bound_arguments(function: Callable, arguments: Arguments) -> BoundArguments:
    return arguments.bind(function)


def test_init(function: Callable, signature: Signature) -> None:
    with pytest.raises(TypeError):
        Arguments().bind(function)

    with pytest.raises(TypeError):
        Arguments("bar", True, "EXTRA").bind(function)

    assert Arguments("bar").bind(function) == BoundArguments(signature, "bar", False)
    assert Arguments("bar", exclaim=True).bind(function) == BoundArguments(signature, "bar", exclaim=True)


def test_asdict(function: Callable) -> None:
    assert Arguments("bar").bind(function).asdict() == {"message": "bar", "exclaim": False}
    assert Arguments("bar", True).bind(function).asdict() == {"message": "bar", "exclaim": True}
    assert Arguments("bar", exclaim=True).bind(function).asdict() == {"message": "bar", "exclaim": True}
    assert Arguments(message="bar", exclaim=True).bind(function).asdict() == {"message": "bar", "exclaim": True}


def test_get(bound_arguments: BoundArguments) -> None:
    assert bound_arguments.get("message") == "foo"

    with pytest.raises(KeyError):
        bound_arguments.get("MISSING")


def test_has(bound_arguments: BoundArguments) -> None:
    assert bound_arguments.has("message")
    assert not bound_arguments.has("MISSING")