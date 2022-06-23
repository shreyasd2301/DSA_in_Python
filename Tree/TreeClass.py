class Node:
    def __init__(self, val) -> None:
        self.data=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self) -> None:
        self.root=None

tree=Tree()
print(tree.root)