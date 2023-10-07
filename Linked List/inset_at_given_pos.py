class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def printlist(head):
    cur=head
    while(cur!=None):
        print(cur.key,end=" ")
        
        cur=cur.next
    print()    
def insertpos(head,pos,key):
    temp=Node(key)
    if pos==1:
        temp.next=head
        return temp
    cur=head
    for i in range(pos-2):
        cur=cur.next
        if cur==None:
            return head
    temp.next=cur.next
    cur.next=temp
    return head                   
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printlist(head)
head=insertpos(head,4,99)
printlist(head)
1 2 3 4 5 