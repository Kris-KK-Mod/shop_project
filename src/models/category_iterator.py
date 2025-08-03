class CategoryIterator:
    """Итератор для перебора товаров категории"""


    def __init__(self, category):
        self.category = category
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        raise StopIteration
