class node:
    def __init__(self,key):
        self.key=key
        self.next=None

def insertsorted(head,x):
    temp= node(x)
    if head==None:
        return temp
    elif head.key>x:
        temp.next=head
        return temp
    
    else:
        cur=head
        while cur.next!=Noe and cur.next.key<x:
            cur=cur.next
        temp.next=cur.next
        cur.next=temp
        return head

def printlist(head):
    cur=head
    while(cur!= None):
        print(cur.key,")
        cur=cur.next
    print()    

head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40) 
printlist(head)
insertsorted(head,25)
printlist(head)        



                    