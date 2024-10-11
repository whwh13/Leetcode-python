import heapq

# 创建一个空堆
heap = []

# 向堆中添加元素
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
heapq.heappush(heap, 4)

# 打印堆
print("Heap:", heap)

# 弹出堆中的最小元素
print("Popped:", heapq.heappop(heap))

# 打印弹出元素后的堆
print("Heap after pop:", heap)