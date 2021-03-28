# js-array
Basic Python module that brings the attributes and methods of a Javascript array to Python.
## Usage
Example usage:
```py
from jsarray import JSArray

array = JSArray(range(10))
(
  array
  .map(lambda item: item**2)
  .filter(lambda item: item % 2 == 0)
  .for_each(print)
)
