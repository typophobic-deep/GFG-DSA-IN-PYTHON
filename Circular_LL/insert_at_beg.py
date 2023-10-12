# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.next=None
# def printlist(head):
#     if head==None:
#         return
#     print(head.key,end="")
#     cur=head.next
#     while cur!=head:
#         print(cur.key,end=" ")
#         cur=cur.next
#     print()    

# def insertbeg(head,key):
#     temp=Node(key)
#     if head==None:
#         temp.next=temp
#         return temp
#     cur=head
    
       
#     while cur.next!=None:
#         cur=cur.next
#     cur.next=temp
#     temp.next=head 
#     return temp
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=head      
# head=insertbeg(head,40) 
# printlist(head)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertBeg(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next

    curr.next = temp
    temp.next = head
    return temp


def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(20)
head.next = Node(30)
head.next.next = head
printCircular(head)

head = insertBeg(head, 10)

printCircular(head)

