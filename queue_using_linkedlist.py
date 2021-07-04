class Node:
  def __init__(self,data):
      self.data=data
      self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        if self.front==None:
            return True
    def enqueue(self,x):
        temp=Node(x)
        if self.rear==None:
            self.rear=self.front=temp
        self.rear.next=temp
        self.rear=temp
    def dequeue(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front=temp.next
        
        if self.front==None:
            self.rear=None

if __name__=="__main__":
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
