from importlib.abc import Traversable


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
        else:
            curl=self.root
            while 1:
                if data>curl.data:
                    if curl.right:
                        curl=curl.right
                    else:
                        curl.right=Node(data)
                        break
                elif data<curl.data:
                    if curl.left:
                        curl=curl.left
                    else:
                        curl.left=Node(data)
                        break
                else: 
                    break

def levelOrder(root):
    global traversal
    traversal=[]
    q=[root]
    while len(q)!=0:
        p=q.pop(0)
        traversal.append(p.data)
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)

tree=BinarySearchTree()
for i in [6,8,7,9,4,3,5]:
    tree.insert(i)

levelOrder(tree.root)
print(traversal)
