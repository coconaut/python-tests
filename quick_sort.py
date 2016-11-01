__author__ = 'coconaut'

# Hoare's partition scheme:
# idea is to move lte to left of pivot, gt to right
# accomplish this by:
#   1. move i to the right until elem >= pivot
#   2. move j to the left until elem <= pivot
#   3. if i <= j, swap, iterate i and j, loop
#   4. if i > j, stop (elems are correct according to the pivot)
#   5. return the pivot index so we know where to split for next recursions


def quicksort(elems):

    def get_pivot(els, lo, hi):
        # just going to take the middle-ish element
        ind = (lo + hi) / 2
        return els[ind]

    def swap(els, a, b):
        tmp = els[a]
        els[a] = els[b]
        els[b] = tmp

    def partition(els, left, right):
        # init
        i, j = left, right
        pivot = get_pivot(els, left, right)

        # loop
        while i <= j:

            while els[i] < pivot:
                i += 1

            while els[j] > pivot:
                j -= 1

            if i <= j:
                swap(els, i, j)
                i += 1
                j -= 1

        # print els

        # return the index on which we'll split
        return i

    def rec_sort(els, left, right):
        # recursive loop -> partition and sort until we reach the same index
            if left < right:
                p = partition(els, left, right)
                rec_sort(els, left, p - 1)
                rec_sort(els, p, right)

    # do it
    start, end = 0, len(elems) - 1
    rec_sort(elems, start, end)

if __name__ == '__main__':

    # random number list
    listy = [1, 12, 5, 26, 7, 14, 3, 7, 2]
    print listy

    # sort
    quicksort(listy)
    print listy

    # TODO: generate the number list to test
    # TODO: functional immutable version (use filter, head tail?)

