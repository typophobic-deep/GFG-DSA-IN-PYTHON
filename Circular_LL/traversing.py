class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def printCLL(head):
    if head==None:
        return None
    print(head.key,end=" ")
    cur=head.next
    while cur!=head:
        print(cur.key,end=" ")
        cur=cur.next
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head      
printCLL(head) 

