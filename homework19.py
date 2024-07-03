class EvenNumbers:
    def __init__(self, a, b):
        self.a = a if a % 2 == 0 else a + 1
        self.b = b
        self.current = 10
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.b:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result

for i in EvenNumbers(10, 25):
    print(i)