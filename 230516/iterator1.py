class ANumbers:
    def __init__(self, start=1.0, end=20):
        self.a = start
        self.e = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.a:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj = ANumbers()
iter = iter(obj)

for x in iter:
    print(x)
