# arguments
Arguments manager

## Usage
### Instantiation
```python
import arguments

args = arguments.Arguments('Hello', 'World', sep=', ')
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