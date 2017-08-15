class Solution(object):
    def find_all_local_maxima(self, arr):
        local_maxs = []
        for i,v in enumerate(arr):
            if i != 0 and i != len(arr) - 1:
                if v >= arr[i - 1] and v >= arr[i + 1]:
                    local_maxs += [i]
        return local_maxs

    def remove_all_local_minima(self, arr_indexes, arr):
        while True:
            index_to_remove = -1
            # print "X", arr_indexes
            for i in xrange(1, len(arr_indexes) - 1):
                index_considered = arr_indexes[i]
                prev_index = arr_indexes[i-1]
                next_index = arr_indexes[i+1]
                # print "Y", index_considered, prev_index, next_index, arr
                if arr[index_considered] <= arr[prev_index] and arr[index_considered] <= arr[next_index]:
                    index_to_remove = i
                    break
            #print "Xs", index_to_remove
            if index_to_remove != -1:
                del arr_indexes[index_to_remove]
            else:
                break
        return arr_indexes

    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """

        heights = [0] + heights + [0]
        all_maxs_indexes = self.find_all_local_maxima(heights)
        print "1", all_maxs_indexes
        wall_indexes = self.remove_all_local_minima(all_maxs_indexes, heights)

        print wall_indexes

        ans = 0
        for i in xrange(len(wall_indexes) - 1):
            a1 = heights[wall_indexes[i]]
            a2 = heights[wall_indexes[i + 1]]
            a_low = min(a1, a2)
            # print a_low
            for j in xrange(wall_indexes[i] + 1, wall_indexes[i + 1]):
                # print a_low, heights[j], ans
                possible_water_fill = a_low - heights[j]
                if possible_water_fill > 0:
                    ans += possible_water_fill

        return ans

s= Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print s.trap([5,4,1,2])
print s.trap([5,1,4,1,2,1,3,2,5]) #[0, 5 ,1, 4 ,1, 2 ,1, 3 ,2, 5 ,0]
print s.trap([5,2,1,2,1,5]) #14
print s.trap([5,5,1,7,1,1,5,2,7,6]) #23
print s.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]) #83
