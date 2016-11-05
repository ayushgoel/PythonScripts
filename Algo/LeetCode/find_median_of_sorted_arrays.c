// https://leetcode.com/problems/median-of-two-sorted-arrays/

#include <stdio.h>
#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int total_nums = nums1Size + nums2Size;
    int *sorted_nums = malloc(total_nums * sizeof(int));
    int i = 0, j = 0, k = 0;
    for (int k = 0; k < total_nums; ++k) {
        if (i == nums1Size) {
            sorted_nums[k] = nums2[j++];
            continue;
        }
        if (j == nums2Size) {
            sorted_nums[k] = nums1[i++];
            continue;
        }
        if (nums1[i] > nums2[j]) {
            sorted_nums[k] = nums2[j++];
        } else {
            sorted_nums[k] = nums1[i++];
        }
    }

    int median_index = total_nums / 2;
    double ans = 0.0;
    if (total_nums % 2 == 0) {
        ans = (sorted_nums[median_index - 1] + sorted_nums[median_index]) / 2.0;
    } else {
        ans = sorted_nums[median_index];
    }
    return ans;
}

int main() {
    int num1 = 2;
    int *nums1 = malloc(num1 * sizeof(int));
    nums1[0] = 1;
    nums1[1] = 2;

    int num2 = 2;
    int *nums2 = malloc(num2 * sizeof(int));
    nums2[0] = 3;
    nums2[1] = 4;

    printf("%f\n", findMedianSortedArrays(nums1, num1, nums2, num2));
}
