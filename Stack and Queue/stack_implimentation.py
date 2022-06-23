class stack:
    def __init__(self):
        self.l=[]

    def push(self, data):
        self.l.append(data)

    def pop(self):
        if len(self.l)!=0:
            return self.l.pop(-1)
        return -1

    def print(self):
        for i in range(len(self.l)-1,-1,-1):
            print(self.l[i],end =" " )
        print()
    
s=stack()
for i in range(5):
    s.push(i)
s.pop()
s.print()