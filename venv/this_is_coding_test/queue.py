from collections import deque

queue = deque()

queue.extend([5,4,3,2,1])

queue.popleft()

print(queue)