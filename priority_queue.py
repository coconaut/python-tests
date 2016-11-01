import sys
import heap_sort as hs


class HeapUnderflowException(Exception):
    def __init__(self):
        super(HeapUnderflowException, self).__init__("The heap's size is less than 1")


class KeyNonIncreaseException(Exception):
    def __init__(self):
        super(KeyNonIncreaseException, self).__init__("The new key is smaller than the current key")


def heap_max(heap):
    return heap.at(0)


def extract_max(heap):
    if heap.heap_size < 1:
        raise HeapUnderflowException
    mx = heap.at(0)
    lst = heap.heap_size - 1
    heap.put(0, heap.at(lst))
    heap.heap_size -= 1
    del heap.array[lst]  # not totally necessary
    hs.max_heapify(heap, 0)
    return mx


def increase_key(heap, i, key):
    if key < heap.at(i):
        raise KeyNonIncreaseException
    heap.put(i, key)
    while i > 0:
        par = hs.parent(i)
        par_val = heap.at(par)
        if par_val < key:
            heap.put(i, par_val)  # bubble up the heap -> NOT WORKING
            heap.put(par, key)
            i = par
        else:
            break


def insert(heap, key):
    new_last_ind = heap.heap_size
    heap.heap_size += 1
    sm = -sys.maxsize - 1
    if heap.heap_size > len(heap):
        heap.array.append(sm)
    else:
        heap.put(new_last_ind, sm)
    increase_key(heap, new_last_ind, key)
