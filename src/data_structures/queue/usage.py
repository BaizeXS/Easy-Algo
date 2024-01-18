from collections import deque

# 初始化队列
deque: deque[int] = deque()

# 元素入队
deque.append(2)
deque.append(5)
deque.append(4)
deque.appendleft(3)
deque.appendleft(1)

# 访问元素
front: int = deque[0]
rear: int = deque[-1]

# 元素出队
pop_front: int = deque.popleft()
pop_rear: int = deque.pop()

# 获取双向队列的长度
size: int = len(deque)

# 判断双向队列是否为空
is_empty: bool = len(deque) == 0
