
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

        if left:
            self.left.parent = self

        if right:
            self.right.parent = self



def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node



if __name__ == '__main__':
    root = Node(1, Node(2), Node(3))
    for y in traverse_in_order(root):
        print(y.value)



