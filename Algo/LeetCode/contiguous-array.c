#include <stdio.h>

int max(int a, int b) {
    return a>b?a:b;
}

int memo[50005][50005];

int findLength(int *nums, int start, int end, int num_zeroes, int num_ones) {
    // printf("%d %d %d %d %d %d\n", start, end, num_zeroes, num_ones, nums[start], nums[end]);
    if (memo[start][end] != 0)
    {
        return memo[start][end];
    }
    if (start == end)
    {
        return 0;
    }
    if (num_zeroes == num_ones)
    {
        memo[start][end] = end-start+1;
    } else if (num_zeroes > num_ones)
    {
        if (nums[start] == 0)
        {
            memo[start][end] = findLength(nums, start + 1, end, num_zeroes - 1, num_ones);
        } else if (nums[end] == 0)
        {
            memo[start][end] = findLength(nums, start, end - 1, num_zeroes - 1, num_ones);
        } else {
            memo[start][end] = max(findLength(nums, start, end - 1, num_zeroes, num_ones - 1),
                                   findLength(nums, start + 1, end, num_zeroes, num_ones - 1));
        }
    } else
    {
        if (nums[start] == 1)
        {
            memo[start][end] = findLength(nums, start + 1, end, num_zeroes, num_ones - 1);
        } else if (nums[end] == 1)
        {
            memo[start][end] = findLength(nums, start, end - 1, num_zeroes, num_ones - 1);
        } else {
            memo[start][end] = max(findLength(nums, start, end - 1, num_zeroes - 1, num_ones),
                                   findLength(nums, start + 1, end, num_zeroes - 1, num_ones));
        }
    }
    return memo[start][end];
}

int findMaxLength(int* nums, int numsSize) {
    if(numsSize <= 1) {
        return 0;
    }
    int num_zeroes = 0, num_ones = 0;
    for (int i = 0; i < numsSize; ++i)
    {
        if (nums[i] == 0)
        {
            num_zeroes++;
        } else
        {
            num_ones++;
        }
    }
    return findLength(nums, 0, numsSize - 1, num_zeroes, num_ones);
}

int main(int argc, char const *argv[])
{
    int x[] = {0,1,0,1,1,1,1};
    printf("%d\n", findMaxLength(x,7));
    // int x[] = {0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1};
    // printf("%d\n", findMaxLength(x,100));
    return 0;
}