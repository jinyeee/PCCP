# 리스트
# 여러개의 데이터를 순서가 있도록 저장

# stack
# 리스트는 리스트인데, 한 방향으로 데이터의 삽입 삭제가 잦은 자료 구조
stack = [1, 2, 3]
stack.append(4)
stack.append(4)
stack.append(4)
stack.pop()
stack.pop()
stack.pop()
# queue
# 리스트는 리스트인데, 다른 방향으로의 데이터 삽입 삭제가 잦은 자료 구조
queue = [1, 2, 3]
queue.append(4)
queue.append(4)
queue.append(4)
queue.pop(0)
queue.pop(0)
queue.pop(0)

from collections import deque

q = deque()
q.append(1)
q.appendleft(2)
q.pop()
q.popleft()








