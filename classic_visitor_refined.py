from abc import ABC


def _qualname(obj):
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    name = _qualname(obj)
    return name[:name.rfind('.')]


_methods = {}


def _visitor_impl(self, arg):
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


def visitor(arg_type):
    def decorator(fun):
        declaring_class = _declaring_class(fun)
        _methods[(declaring_class, arg_type)] = fun

        return _visitor_impl

    return decorator


class DoubleExpression:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    def __str__(self):
        return ''.join(self.buffer)

    @visitor(DoubleExpression)
    def visit(self, de):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        # ae.left.accept(self)
        self.visit(ae.left)
        self.buffer.append('+')
        # ae.right.accept(self)
        self.visit(ae.right)
        self.buffer.append(')')


class ExpressionEvaluator:
    def __main__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value

    @visitor(AdditionExpression)
    def visitor(self, ae):
        self.visit(ae.left)
        temp = self.value
        self.visit(ae.right)
        self.value += temp


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    printer = ExpressionPrinter()
    printer.visit(e)
    print(printer)

    evaluator = ExpressionEvaluator()

    evaluator.visit(e)
    print(f'{printer} = {evaluator.value}')
