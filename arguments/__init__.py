import dataclasses
import itertools
import typing


# TODO: Make `args` and `kwargs` immutable?
@dataclasses.dataclass
class Arguments:
    args: typing.Tuple[typing.Any] = dataclasses.field(default_factory=tuple)
    kwargs: typing.Dict[str, typing.Any] = dataclasses.field(default_factory=dict)

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        self.args = args
        self.kwargs = kwargs

    def __str__(self) -> str:
        return ", ".join(
            itertools.chain(
                (f"{arg!r}" for arg in self.args),
                (f"{key}={value!r}" for key, value in self.kwargs.items()),
            ),
        )

    def __repr__(self) -> str:
        return "{class_name}({arguments})".format(
            class_name=type(self).__name__,
            arguments=", ".join(
                itertools.chain(
                    (f"{arg!r}" for arg in self.args),
                    (f"{key}={value!r}" for key, value in self.kwargs.items()),
                ),
            ),
        )

    def __iter__(self) -> typing.Iterable[typing.Any]:
        value: typing.Any
        for value in itertools.chain(self.args, self.kwargs.values()):
            yield value

    def __getitem__(self, index: int) -> typing.Any: # TODO: Support slices
        return list(self)[index]

    def __len__(self) -> int:
        return len(list(self))

    def __call__(self, func: typing.Callable) -> typing.Any:
        return func(*self.args, **self.kwargs)