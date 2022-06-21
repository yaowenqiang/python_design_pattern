# OCP(Open Close Principle)
from enum import Enum

class Color(Enum):
    READ = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3



class Product:

    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name



class ProductFilter:

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p


    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


    def filter_by_size_and_size(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


# Enterprise pattenr (specification pattern)


class Specification:
    def is_satificied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter(slef, items, specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satificied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satificied(self, item):
        return item.size == self.size


class BatterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satificied(item):
                yield item


class AndSpecification(Specification):
    def  __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2


    def is_satificied(self, item):
        return self.spec1.is_satificied(item) and \
            self.spec2.is_satificied(item)




apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()

for p in pf.filter_by_color(products, Color.GREEN):
    print(f'- {p.name} is green')


bf = BatterFilter()
print('Green products: ')

green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f'- {p.name} is green')

print('Green products: ')
large = SizeSpecification(Size.LARGE)

for p in bf.filter(products, large):
    print(f'- {p.name} is large')


print('Large blue items')

# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue = large and  ColorSpecification(Color.BLUE)

for p in bf.filter(products, large_blue):
    print(f'- {p.name} is large and blue')
