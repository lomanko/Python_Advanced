class FlatIteratorAny:

    def __init__(self, list_):
        self.list_ = list_
        self.new_list = []

    def __iter__(self):
        self.position = - 1
        self.list_to_iterate = self.flatten_list(self.list_)
        return self

    def __next__(self):
        self.position += 1
        if self.position > len(self.list_to_iterate) - 1:
            raise StopIteration
        return self.list_to_iterate[self.position]

    def flatten_list(self, list_):  # преобразование листа любой вложенности в плоский лист
        counter = 0
        while counter < len(list_):
            if type(list_[counter]) is not list:
                self.new_list.append(list_[counter])
                counter += 1
            else:
                self.flatten_list(list_[counter])
                counter += 1
        return self.new_list
