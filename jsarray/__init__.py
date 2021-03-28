from pandas.core.common import flatten


class JSArray(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def length(self):
        return len(self)

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
        return JSArray(flatten(self))
