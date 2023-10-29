from collections import deque
stack= deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
top=stack[-1]
size=len(stack)
print(top)
print(size)