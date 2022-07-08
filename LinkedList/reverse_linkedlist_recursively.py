from LinkedList import singly_linked_list

def reverseList(head):
        if head:
            if head.next==None:
                return head
        newhead=reverseList(head.next)
        temp=newhead
        while temp.next:
            temp=temp.next
        temp.next=head
        head.next=None
        return newhead

l=singly_linked_list.LinkedList()
for i in [1, 2, 3, 4]:
    l.insertAtStart(i)
l.printLL()
l2=singly_linked_list.LinkedList()
l2.head=reverseList(l.head)
l2.printLL()