class node:
    def __init__(self,key):
        self.key=key
        self.next=None
def insert(head,key):
    temp=node(key)
    temp.next=head
    return temp
def printlist(head):
    cur=head
    while(cur!=None):
        print(cur.key,end=" ")
        cur=cur.next

head=None
head=insert(head,10)
head=insert(head,20)
head =insert(head,30)
printlist(head)
