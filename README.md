# arguments
Arguments manager

## Usage
### `Arguments`
#### Instantiation
```python
from arguments import Arguments

args = Arguments("Hello", "World", sep=", ")
```
```python
>>> args
Arguments("Hello", "World", sep=", ")
```

#### Attributes
```python
>>> args.args
("Hello", "World")
>>> args.kwargs
{"sep": ", "}
```

#### Iteration
```python
>>> tuple(args)
("Hello", "World", ", ")
>>> len(args)
3
```

#### Invokation
```python
>>> args.call(print)
Hello, World
```

#### Partial
```python
>>> func = args.partial(print, end="!")
>>> func(sep="-")
hello-world!
```

#### Union
```python
>>> Arguments("hello", sep=", ") | Arguments("world", sep="-")
Arguments("hello", "world", sep="-")
```

### `BoundArguments`
#### Instantiation
```python
from arguments import Arguments, BoundArguments

def foo(message: str, exclaim: bool = False) -> None:
    ...

args: Arguments = Arguments("Hello, World")
bound_args: BoundArguments = args.bind(foo)
```
```python
>>> bound_args
BoundArguments("Hello, World", False)
```

#### As Dictionary
```python
>>> bound_args.asdict()
{"message": "Hello, World", "exclaim": False}
```

#### Get
```python
>>> bound_args.get("message")
"Hello, World"
```

#### Has
```python
>>> bound_args.has("message")
True
```