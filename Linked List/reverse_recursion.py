class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def reverse(prev,cur):
    if cur==None:
        return prev
   
    temp=cur.next
    cur.next=prev
    
    return reverse(cur,temp)
def printlist(head):
    cur=head
    while cur!=None:
        print(cur.key,end=" ")
        cur=cur.next
head= Node(10)
head.next= Node(20)
head.next.next= Node(30)
head.next.next.next=Node(40) 

printlist(head)
reversed_head = reverse(None,head)  # Store the reversed list in a different variable

print("Reversed linked list:")
printlist(reversed_head)