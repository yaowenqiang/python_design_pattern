class GraphObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphObject):
    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphObject()
    drawing._name = "My Drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Circle("Yellow"))

    group = GraphObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))

    drawing.children.append(group)

    print(drawing)
