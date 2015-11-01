__author__ = 'coconaut'


def _merge(left, right):
    res = []
    # merge the two sorted halves, comparing one elem at a time
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    # add the remaining of either surviving set to result, return it
    return res + left + right


def mergesort(elems):
    length = len(elems)

    # if 1 or less, sorted
    if length <= 1:
        return elems

    # divide
    mid = length / 2
    left = elems[0:mid]
    right = elems[mid:]

    # recursively divide / merge
    left = mergesort(left)
    right = mergesort(right)

    # merge the two sorted halves
    return _merge(left, right)


if __name__ == '__main__':

    # random number list
    listy = [1, 12, 5, 26, 7, 14, 3, 7, 2]
    print listy

    # sort
    sorted = mergesort(listy)
    print sorted
