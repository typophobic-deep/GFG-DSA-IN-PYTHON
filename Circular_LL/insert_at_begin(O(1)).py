class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def printlist(head):

    if head==None:
        return
    print(head.key,end=" ")
    cur=head.next
    while cur!=head:
        print(cur.key,end=" ")
        cur=cur.next
    print()
def insertatend(head,key):

    temp=Node(key)
    if head == None:
        temp.next=temp
        return temp   
    cur=head
    temp.next=cur.next
    cur.next=temp
    temp.key,cur.key=cur.key,temp.key
    return cur
head = Node(20)
head.next = Node(30)
head.next.next = head
printlist(head)
head = insertatend(head, 10)

printlist(head)
         