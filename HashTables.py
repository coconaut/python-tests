__author__ = 'Alexander'

# Hash Table practice. Yes, I know that Python dictionaries are built-in hashtables.

class HashTable:
    # TODO: resizing?
    def __init__(self, size, hash_func):
        self.buckets = [None]*size
        self.hash = hash_func

    def get(self, key):
        idx = self.hash(key)
        bucket = self.buckets[idx]
        if bucket is not None:
            for (k, v) in bucket:
                if k == key:
                    return v
        return None

    def set(self, key, value):
        idx = self.hash(key)
        if self.buckets[idx] is None:
            # first in bucket
            self.buckets[idx] = [(key, value)]
        else:
            # see if we need to overwrite or append
            update = False
            for i in range(0, len(self.buckets[idx])):
                (k, v) = self.buckets[idx][i]
                if k == key:
                    # updating the value
                    self.buckets[idx][i] = (key, value)
                    update = True
                    break
            # otherwise, not found / collision -> add it
            if not update:
                self.buckets[idx].append((key, value))


# could make higher order with functools partial
def hasher(size):
    # create a closure with size set
    def actual_hash(key):
        total = reduce(lambda acc, i: acc + ord(i), [c for c in key], 0)
        # use module to find index
        return total % size
    return actual_hash

if __name__ == '__main__':
    # create hash table
    list_size = 10
    hashing_func = hasher(list_size)
    table = HashTable(10, hashing_func)

    # set some key/ values
    table.set("apple", 3)
    table.set("zebra", 5)

    # test it
    assert table.get("zebra") == 5
    assert table.get("apple") == 3

    # try a collision
    table.set("lapep", 8)
    assert table.get("apple") == 3
    assert table.get("lapep") == 8

