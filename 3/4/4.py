from typing import overload, SupportsIndex


class DefaultList(list):

    def __init__(self, default):

        self.default = default

        super().__init__(self)

    def __getitem__(self, y: SupportsIndex):
        try:
            return super().__getitem__(y)
        except IndexError:

            return self.default


s = DefaultList(5)
s.extend([4, 10])
indexes = [1, 124, 1882]
for i in indexes:
    print(s[i], end=" ")

print("\n")

s = DefaultList(51)
s.extend([1, 5, 7])
indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")
