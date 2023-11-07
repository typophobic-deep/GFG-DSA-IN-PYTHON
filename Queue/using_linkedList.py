class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None 
        self.size=0

    def size(self):
        return self.size
    def isempty(self):
        if self.size==0:
            return True
        return False
    def getfront(self):
        return self.front.key
    def getrear(self):
        return self.rear.key
    def enque(self,x):
        temp=Node(x)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.size+=1
    def deque(self):
        if self.front==None:
            return None
        else:
            result=self.front.key
            self.front=self.front.next
            if self.front==None:
                self.rear=None
        self.size-=1
        return result
q=Queue()
q.enque(10)
print(q.getfront(), q.getrear())
q.enque(20)
print(q.getfront(), q.getrear())
q.enque(30)
print(q.getfront(), q.getrear())
q.deque()
print(q.getfront(), q.getrear())

