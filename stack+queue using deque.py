class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        return True if self.front==None else False
    def insert_first(self,value):
        new=Node(value)
        if self.front==None:
            self.front=new
            self.rear=new
        temp=self.front
        temp.prev=new 
        new.next=temp
        self.front=new
    def insert_last(self,value):
        new=Node(value)
        if self.rear==None:
            self.rear=new
            self.front=new
        temp=self.rear
        temp.next=new
        new.prev=temp
        self.rear=new
    def remove_first(self):
        x=self.front
        self.front=self.front.next
        self.front.prev=None
        return x
    def remove_last(self):
        x=self.rear
        self.rear=self.rear.prev
        self.rear.next=None
        return x
    def display(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next
class Stack(Deque):
    def __init__(self):
        Deque.__init__(self)
    def push(self,value):
        self.insert_last(value)
    def pop(self):
        self.remove_last()
    def display1(self):
        self.display()
if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.display1()
    s.pop()
    s.display1()

            




