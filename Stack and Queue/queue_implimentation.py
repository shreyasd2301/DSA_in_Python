class Queue:
    def __init__(self):
        self.l=[]

    def enque(self, data):
        self.l.append(data)

    def deque(self):
        if len(self.l)!=0:
            return self.l.pop(0)
        return -1

    def print(self):
        for i in range(len(self.l)):
            print(self.l[i],end =" " )
        print()
    
q=Queue()
for i in range(5):
    q.enque(i)
q.deque()
q.print()