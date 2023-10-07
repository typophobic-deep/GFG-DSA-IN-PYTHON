class node:
    def __init__(self,k):
        self.key=k
        self.next=None
def printlist(head,x):
    cur= head
    pos=1
    while(cur!=None):
        if cur.key == x:
            return pos
        else:
            pos+=1
            cur=cur.next
    return -1        
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
x=0
print(printlist(head,x))