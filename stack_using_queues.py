from queue import Queue
class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.cursize=0
    def push(self,x):
        self.q2.put(x)
        self.cursize+=1
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
            
        temp=self.q1
        self.q1=self.q2
        self.q2=temp
    def pop(self):
        #self.q1.get()
        self.q1.get()
        self.cursize-=1
        
    def size(self):
        print(self.cursize)
    def printq(self):
       
        for i in range(self.q1.qsize()):
            print(self.q1.queue[i])
            
if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.printq()
    s.size()
    s.pop()
    s.size()
    s.printq()