class FlatIterator:

    def __init__(self, list_):
        self.list_ = list_
        self.flatten_list = sum(list_, [])

    def __iter__(self):
        self.position = - 1
        return self

    def __next__(self):
        self.position += 1
        if self.position > len(self.flatten_list) - 1:
            raise StopIteration
        return self.flatten_list[self.position]
