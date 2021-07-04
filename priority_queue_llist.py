class Node:
    def __init__(self,data,priority):
        self.data=data
        self.pr=priority
        self.next=None
class Pqueue:
    def __init__(self):
        self.head=None
    def push(self,value,priority):
        new=Node(value,priority)
        if self.head==None:
            self.head=new
        elif self.head.pr<new.pr:
            new.next=self.head
            self.head=new
        else:
            temp=self.head
            while temp.next != None and temp.next.pr>=new.pr:
                temp=temp.next
            new.next=temp.next
            temp.next=new
    def pop(self):
        if self.head==None:
            return
        x=self.head.data
        self.head=self.head.next
        return x
    def peek(self):
        return self.head.data
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    pq=Pqueue()
    pq.push(1,1)
    pq.push(4,4)
    pq.push(3,3)
    pq.push(5,5)
    pq.display()
    pq.pop()
    pq.display()
    pq.push(6,6)
    pq.display()