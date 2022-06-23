class Stack:
    def __init__(self):
        self.st = []
    
    def push(self,data):
        self.st.append(data)

    def pop(self):
        popEle = -1
        if len(self.st)>0:
            popEle = self.st.pop(-1)
        return popEle

class Queue:
    def __init(self):
        self.st=[]