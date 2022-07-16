# arguments
Arguments manager

## Usage
### Instantiation
```python
from arguments import Arguments

args = Arguments('Hello', 'World', sep=', ')
```
```python
>>> args
Arguments('Hello', 'World', sep=', ')
```

### Attributes
```python
>>> args.args
('Hello', 'World')
>>> args.kwargs
{'sep': ', '}
```

### Iteration
```python
>>> tuple(args)
('Hello', 'World', ', ')
>>> len(args)
3
```

### Invokation
```python
>>> args(print)
Hello, World
```

### Union
```python
>>> Arguments("hello", sep=", ") | Arguments("world", sep="-")
Arguments("hello", "world", sep="-")
```