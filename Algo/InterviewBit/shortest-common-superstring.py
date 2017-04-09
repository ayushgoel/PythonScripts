# https://www.interviewbit.com/problems/shortest-common-superstring/

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        a = [i for i in A]
        while True:
            item_to_remove = None

            max_overlap = None
            for i in xrange(len(a)):
                for j in xrange(i + 1, len(a)):
                    item_to_remove = self.substring(a[i], a[j])
                    if item_to_remove is not None:
                        break

                    ol = self.overlap(a[i], a[j])
                    if max_overlap is None:
                        max_overlap = ol
                    elif max_overlap is not None and max_overlap['length'] < ol['length']:
                        max_overlap = ol

                if item_to_remove is not None:
                    a.remove(item_to_remove)
                    break

            if max_overlap is not None:
                replacement_string = max_overlap['el1'] + max_overlap['el2'][max_overlap['length']:]
                a.remove(max_overlap['el1'])
                a.remove(max_overlap['el2'])
                a.append(replacement_string)

            if len(a) == 1:
                return len(a[0])

    def substring(self, a, b):
        if a.find(b) != -1:
            return b
        elif b.find(a) != -1:
            return a
        return None

    def overlap(self, a, b):
        l1 = self.overlap_length(a, b)
        l2 = self.overlap_length(b, a)
        if l1 > l2:
            return {'length': l1, 'el1': a, 'el2': b}
        else:
            return {'length': l2, 'el1': b, 'el2': a}

    def overlap_length(self, a, b):
        length = 0
        for i in xrange(len(a)):
            x = len(a) - i
            if a[x:] == b[:i]:
                length = i
        return length


if __name__ == '__main__':
    s = Solution()
    print s.solve(["abcd", "cdef", "fgh", "de"])
    # print s.solve(["asd", "fgh", "asdf", "fgh", "asdf", "sdfx"])
