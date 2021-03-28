try:
    from pandas.core.common import flatten
except ImportError:
    flatten = None


class JSArray(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index_of = self.index
        self.concat = self.extend

    @property
    def length(self):
        return len(self)

    @property
    def sum(self):
        """ This is not in Javascript, but it would be useful to have """
        return sum(self)

    def push(self, *items):
        self.extend(items)
        return self

    def slice(self, start=None, end=None):
        return self[slice(start, None, end)]

    def map(self, key):
        return JSArray(key(_) for _ in self)

    def for_each(self, callback):
        self.map(callback)
        return self

    def filter(self, key):
        return JSArray(_ for _ in self if key(_))

    def find(self, key):
        _result = self.filter(key)
        if len(_result) <= 0:
            return None
        return _result[0]

    def flat(self):
        if not flatten:
            raise ImportError("The pandas module is required to use this method.")

        return JSArray(flatten(self))

    def join(self, delimiter):
        return delimiter.join(self)

    def some(self, key):
        return self.find(key) is not None

    def shift(self):
        return self.pop(0)

    def unshift(self, *elements):
        for element in elements:
            self.insert(0, element)
        return self

    def values(self):
        return iter(self)

    def find_index(self, key):
        try:
            return self.index(self.find(key))
        except ValueError:
            return None
