#method1
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def dequeue(self):
        if len(self.s1)==0:
            print("q is empty")
        x=self.s1[-1]
        self.s1.pop()
        print(x)

if __name__=='__main__':
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()

#method2 -better
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        self.s1.append(x)
    def dequeue(self):
        if len(self.s1)==0 and len(self.s2)==0:
            print("error")
        if len(self.s2)==0:
            while len(self.s1)!=0:
                self.s2.append(self.s1[-1])
        x=self.s2[-1]
        self.s2.pop()
        return x
    #using recursion 
    def dequeue(self):
        if len(self.s)<=0:
            print("error")
            return
        x=self.s[len(self.s)-1]
        self.s.pop()
        if len(self.x)<=0:
            return x
        item=self.dequeue()
        self.s.append(x)
        return item


