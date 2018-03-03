import collections

class Solution(object):

    def gen_primes(self):
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}

        # The running integer that's checked for primeness
        q = 2

        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                #
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                #
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            q += 1

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums

        all_primes_generator = self.gen_primes()
        all_primes = [all_primes_generator.next()]
        all_primes_dict = collections.defaultdict(set)

        hasOne = False
        for num in nums:
            if num != 1:
                while all_primes[-1] < num:
                    all_primes.append(all_primes_generator.next())
                for prime in all_primes:
                    if num % prime == 0:
                        all_primes_dict[prime].add(num)
                    if prime > num:
                        break
            else:
                hasOne = True

        # print all_primes_dict[2]
        # print all_primes_dict

        if hasOne:
            for k,v in all_primes_dict.iteritems():
                v.add(1)
            all_primes_dict[1].add(1)

        print all_primes_dict

        max_len = 0
        max_set = None
        for item in all_primes_dict.itervalues():
            if len(item) > max_len:
                max_len = len(item)
                max_set = item

        if max_set:
            return list(max_set)
        else:
            return []

s = Solution()
print s.largestDivisibleSubset([1,2,3])
print s.largestDivisibleSubset([1,2,4,8])
print s.largestDivisibleSubset([1])
print s.largestDivisibleSubset([546,669])

