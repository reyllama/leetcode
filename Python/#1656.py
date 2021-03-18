
"""
1656. Design an Ordered Stream

There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.
"""

class OrderedStream:

    def __init__(self, n: int):
        self.base = [[]] * n
        self.idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:


        self.base[idKey-1] = [value]

        x = self.base[self.idx]

        if len(x) > 0:
            if self.idx == len(self.base)-1:
                return self.base[self.idx]
            j = self.idx + 1
            while len(self.base[j]) > 0:
                x += self.base[j]
                if j == len(self.base)-1:
                    return x
                j += 1
            self.idx = j
        return x

"""
Runtime: 228 ms, faster than 36.71% of Python3 online submissions for Design an Ordered Stream.
Memory Usage: 14.9 MB, less than 95.79% of Python3 online submissions for Design an Ordered Stream.
"""
