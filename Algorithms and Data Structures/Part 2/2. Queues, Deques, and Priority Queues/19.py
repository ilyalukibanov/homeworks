def insert(heap, value):
    heap.append(value)
    index = len(heap) - 1
    while index > 0 and heap[index] > heap[(index-1) // 2]:
        heap[index], heap[(index-1) // 2] = heap[(index-1) // 2], heap[index]
        index = (index-1) // 2
    return None


def extract(heap):
    largest = heap[0]
    HEAP_SIZE = len(heap)-1
    heap[0] = heap[-1]
    index = 0
    while index*2+1 < HEAP_SIZE:
        max_child_index = index *2 + 1
        if heap[index*2+2] > heap[max_child_index]:
            max_child_index += 1
        if heap[index] < heap[max_child_index]:
            heap[index], heap[max_child_index] = heap[max_child_index], heap[index]
            index = max_child_index
        else:
            break
    heap.pop()
    return largest

heap = []
with open('input.txt', 'r') as file:
    N = int(file.readline())
    for i in range(N):
        s = file.readline()
        if len(s) == 2:
            print(extract(heap))
        else:
            insert(heap, int(s.split()[1]))