# arguments
Arguments manager

## Usage
```python
>>> import arguments
>>>
>>> args = arguments.Arguments('Hello', 'World', sep=', ')
>>>
>>> args
Arguments('Hello', 'World', sep=', ')
>>>
>>> args.args
('Hello', 'World')
>>> args.kwargs
{'sep': ', '}
>>>
>>> len(args)
3
>>> tuple(args)
('Hello', 'World', ', ')
>>>
>>> args(print)
Hello, World
```