"""
Maximum sub-array problem.
[Chapter 4, Section 4.1.

Given an array of positive and negative integers,
find the maximum sub-array.
"""


class MaxSubArray:
    def __init__(self, arr):
        self.array = arr

    def divide_and_conquer(self):
        # solves in Theta(nlogn)
        return self._find_max_sub_array(0, len(self.array) - 1)

    def _find_max_sub_array(self, low, high):
        if high == low:
            return low, high, self.array[low]  # base case of 1 element
        else:
            mid = (low + high) / 2             # should already truncate -> want floor
            (left_low, left_high, left_sum) = self._find_max_sub_array(low, mid)
            (right_low, right_high, right_sum) = self._find_max_sub_array(mid + 1, high)
            (cross_low, cross_high, cross_sum) = self._find_max_crossing_sub_array(low, mid, high)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum

    def _find_max_crossing_sub_array(self, low, mid, high):
        left_max = mid  # default to mid
        left_sum = self.array[mid]
        tot = 0
        for i in range(mid, low - 1, -1):
            tot += self.array[i]
            if tot > left_sum:
                left_sum = tot
                left_max = i
        right_max = mid + 1
        right_sum = self.array[mid + 1]
        tot = 0
        for j in range(mid + 1, high + 1):
            tot += self.array[j]
            if tot > right_sum:
                right_sum = tot
                right_max = j
        return left_max, right_max, left_sum + right_sum

    def solve_straight_through(self):
        # should solve in Theta(n)
        max_ending_here = max_so_far = self.array[0]
        tmp_start = start = end = 0

        for i in range(1, len(self.array)):
            nxt = self.array[i]
            running_tot = max_ending_here + nxt

            # the max of this section is either the next element or the running total
            max_ending_here = max(nxt, running_tot)

            # if the next element is an improvement over the running_tot,
            # then it is time to start a new subarray
            if nxt > running_tot:  # we're just at this one element
                tmp_start = i

            # see if we improved overall
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here  # update the current max
                end = i  # adjust the end index
                start = tmp_start  # make sure the start is accurate

        return start, end, max_so_far


def test(arr):
    m = MaxSubArray(arr)
    print "divide and conquer: %i %i %i" % m.divide_and_conquer()
    print "straight through %i %i %i" % m.solve_straight_through()


def run_tests():
    inputs = [
        [1, 2, 3, -2, 4, 6, -4, 1],
        [-5, 3, 5, 7, -18, 9, 1, 3, 7, -6],
        [3, 4, 5, -5, -5, -5, -5, 7],
        [3, 4, 5, -5, -5, -5, -5, 400]
    ]
    for arr in inputs:
        test(arr)
