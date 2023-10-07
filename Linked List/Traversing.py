class node:
    def __init__(self,k):
        self.key=k
        self.next=None
def printlist(head):
    cur= head
    while(cur!=None):
        print(cur.key,end=" "  )
        cur=cur.next
        




head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
printlist(head)