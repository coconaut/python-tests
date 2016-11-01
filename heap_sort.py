class Heap:
    def __init__(self, arr):
        self.array = arr
        self.heap_size = len(arr)

    def __len__(self):
        return len(self.array)

    def at(self, i):
        return self.array[i]

    def put(self, i, val):
        self.array[i] = val


def parent(i):
    return (i - 1) / 2  # will take floor anyway


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def in_heap(heap, i):
    return i <= heap.heap_size - 1


def max_heapify(heap, i):
    l = left(i)
    r = right(i)
    largest_idx = i
    if in_heap(heap, l) and heap.at(l) > heap.at(i):
        largest_idx = l
    if in_heap(heap, r) and heap.at(r) > heap.at(largest_idx):
        largest_idx = r
    if largest_idx != i:
        tmp = heap.at(i)
        largest = heap.at(largest_idx)
        heap.put(i, largest)
        heap.put(largest_idx, tmp)
        max_heapify(heap, largest_idx)


def build_max_heap(arr):
    heap = Heap(arr)
    mid = len(heap) / 2  # will take floor anyway
    for i in range(mid, -1, -1):
        max_heapify(heap, i)
    return heap


def heap_sort(arr):
    heap = build_max_heap(arr)
    for i in range(len(heap) - 1, 0, -1):
        tmp = heap.at(i)
        fst = heap.at(0)
        heap.put(i, fst)
        heap.put(0, tmp)
        heap.heap_size -= 1
        max_heapify(heap, 0)


def test():
    arr = [1, 7, 4, 8, 2, 12, 45, 0, 4]
    print "unsorted: ", arr, "\n"
    heap_sort(arr)
    print "sorted: ", arr
