class Node:
    def __init__(self, val) -> None:
        self.data=val
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def insert(self, data):
        if self.root==None:
            self.root=Node(data)
        curl=self.root
        while 1:
            if data>curl.data:
                if curl.right:
                    curl=curl.right
                else:
                    curl.rigth=Node(data)
                    break
            if data<curl.data:
                if curl.left:
                    curl=curl.left
                else:
                    curl.left=Node(data)
                    break
            else:
                break


tree=BinarySearchTree()
for i in [6,7,8,9,3,5]:
    tree.insert(i)
print(tree.root.data)