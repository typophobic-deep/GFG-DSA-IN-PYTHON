from collections import deque
lst= deque()
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)
print(lst.popleft())
lst.append(40)
print(lst.popleft())
print(lst[0])
print(lst[-1])

