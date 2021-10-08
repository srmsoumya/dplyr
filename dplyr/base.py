import copy


class Dplyr:
    def __init__(self, blob: None):
        self.blob = [] if blob is None else blob

    def __repr__(self):
        return f"Blob: # {len(self)}, Headers: {list(self.blob[0].keys())}"

    def __len__(self):
        return len(self.blob)

    def pipe(self, *fns):
        data = copy.deepcopy(self.blob)
        for fn in fns:
            data = [b for b in data if fn(b)]
        return Dplyr(data)

    def mutate(self, **kwargs):
        data = copy.deepcopy(self.blob)

        for key, fn in kwargs.items():
            for b in data:
                b[key] = fn(b)

        return Dplyr(data)

    def select(self, *cols: str):
        return Dplyr([{col: b[col] for col in cols} for b in self.blob])

    def sort(self, *cols, reverse=False):
        return Dplyr(
            sorted(self.blob, key=lambda x: [x[col] for col in cols], reverse=reverse)
        )

    def head(self, n: int = 5):
        return Dplyr(self.blob[:n])

    def tail(self, n: int = 5):
        if n == 0:
            return Dplyr([])
        else:
            return Dplyr(self.blob[-n:])

    def collect(self):
        return self.blob
