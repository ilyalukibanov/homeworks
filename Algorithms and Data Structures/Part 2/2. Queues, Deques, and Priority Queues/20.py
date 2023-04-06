def heapify(heap):
    HEAP_SIZE = len(heap)-1
    for index in range(len(heap) // 2 + 1, -1, -1):
        position = index
        while position*2+1 <= HEAP_SIZE:
            max_child_index = position*2 + 1
            if (position*2+2 <= HEAP_SIZE) and (heap[position*2+2] > heap[max_child_index]):
                max_child_index += 1
            if heap[position] < heap[max_child_index]:
                heap[position], heap[max_child_index] = heap[max_child_index], heap[position]
            position = max_child_index
    return None


def heap_sort(heap):
    last_element = len(heap)-1
    while last_element > 0:
        heap[last_element], heap[0] = heap[0], heap[last_element]
        last_element -= 1
        index = 0
        while index*2+1 <= last_element:
            max_child_index = index*2 + 1
            if (index*2+2 <= last_element) and (heap[index*2+2] > heap[max_child_index]):
                max_child_index += 1
            if heap[index] < heap[max_child_index]:
                heap[index], heap[max_child_index] = heap[max_child_index], heap[index]
                index = max_child_index
            else:
                break

heap = []
with open('input.txt', 'r') as file:
    N = int(file.readline())
    heap = list(map(int, file.readline().split()))
    heapify(heap)
    heap_sort(heap)
    print(*heap)