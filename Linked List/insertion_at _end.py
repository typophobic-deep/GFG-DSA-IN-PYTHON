class node:
    def __init__(self,key):
        self.key=key
        self.next=None
def insertend(head,key):
    if head == None:
        return node(key)
    cur=head
    while(cur.next!=None):
        cur=cur.next
    cur.next=node(key)
    return head
def printlist(head):
    cur=head
    while(cur!=None):
        print(cur.key,end=" ")
        cur=cur.next
head = None

while True:
    user_input = input("Enter a number to insert (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    try:
        number = int(user_input)
        head = insertend(head, number)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display the linked list
print("Linked List:")
printlist(head)                   

