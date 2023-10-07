class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printlist(head):
    cur = head
    while(cur!=None):
        print(cur.key,end=" ")
        cur=cur.next
    print()
def delete(head):
    if head==None:
        return None
    else:
        return head.next  
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
printlist(head)
head=delete(head)
printlist(head)
            