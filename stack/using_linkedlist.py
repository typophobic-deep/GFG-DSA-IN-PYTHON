class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.size+=1
    def sizee(self):
        return self.size
    def peek(self):
        if self.head==None:
            print("underflow condition")
        return self.head.data
    def pop(self):
        if self.head==None:
            print(" no element to delete")
        ele=self.head.data    
        self.head=self.head.next    
        self.size-=1
        return ele
    def print1(self):
        cur=self.head
        while cur!=None:
            print(cur.data,end=" ")
            cur=cur.next
        print("None")    
s= stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.print1()   
print(s.pop())
s.peek()
s.sizee()
print(s.pop())
s.sizee()
s.print1()
