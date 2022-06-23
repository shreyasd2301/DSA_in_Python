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

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    traversal.append(root.data)
    inorder(root.right)

def preorder(root):
    if root==None:
        return
    traversal.append(root.data)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if root==None:
        return
    
    postorder(root.left)
    postorder(root.right)
    traversal.append(root.data)

tree=BinarySearchTree()
for i in [6,8,7,9,4,3,5]:
    tree.insert(i)

global traversal
# inoder
traversal=[]
root=tree.root
inorder(root)
print(traversal)
#preorder
traversal=[]
root=tree.root
preorder(root)
print(traversal)
#post Order
traversal=[]
root=tree.root
postorder(root)
print(traversal)