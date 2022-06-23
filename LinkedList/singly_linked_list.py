class Node:
    def __init__(self, data):
        self.val=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtStart(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def insertAtkthPosition(self,data, k):

        newNode=Node(data)
        head1=self.head
        if k==2:
            head1=head1.next
        else:
            for i in range(k-2):
                head1=head1.next
        head2=head1.next
        newNode.next=head2
        head1.next=newNode

    def insertAtEnd(self,data):
        newNode=Node(data)
        head=self.head
        while(head.next!=None):
            head=head.next
        head.next=newNode

    def printLL(self):
        head=self.head
        while (head!=None):
            print(head.val, end=" ")
            head=head.next

    def deleteAtStart(self):
        if self.head.next:
            head=self.head.next
            self.head=head
        else:    
            self.head=None
    
    def deleteANode(self, posNode):
        head=self.head
        while (head.next!=posNode):
            head=head.next
        head.next=posNode.next
    
    def search(self, nodeValue):
        head=self.head
        while (head!=None):
            if head.val==nodeValue:
                return head
            head=head.next

    def length(self, head):
        if head==None:
            return 0
        return 1+self.length(head.next)

l=LinkedList()
for i in [1, 2, 3, 4]:
    l.insertAtStart(i)
l.printLL()
print(l.length(l.head))
# l.deleteANode(l.search(3))
# l.printLL()

# l.insertAtEnd(9)
# l.printLL()
# print(l.head.val)
# l.insertAtkthPosition(5,3)
# l.deleteAtStart()