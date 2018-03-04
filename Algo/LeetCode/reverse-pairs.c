#include<stdio.h>
#include<stdlib.h>

int ans = 0;

void findAns(int *nums, int s1, int e1, int s2, int e2) {
    while(s1 != e1 && s2 != e2) {
        if ((nums[s1]/2 > nums[s2]) || (nums[s1]/2 == nums[s2] && nums[s1]%2 == 1)) {
            //printf("SS %d %d %d %d\n", nums[s1], s1, nums[s2], s2);
            ans += e1-s1;
            s2++;
        } else {
            s1++;
        }
    }
}

void merge(int *nums, int s1, int e1, int s2, int e2) {
    int length = e1-s1 + e2-s2;
    //printf("T %d %d %d %d L%d\n", s1, e1, s2, e2, length);
    int x1 = s1, x2 = s2;
    findAns(nums, s1, e1, s2, e2);
    int *arr = malloc(length * sizeof(int));
    for (int i = 0; i < length; ++i) {
        if (x1 == e1) {
            arr[i] = nums[x2++];
        } else if (x2 == e2) {
            arr[i] = nums[x1++];
        } else if (nums[x1] > nums[x2]) {
            arr[i] = nums[x2++];
        } else {
            arr[i] = nums[x1++];
        }
    }
    for (int i = 0; i < length; ++i)
    {
        //printf("x %d ", arr[i]);
        nums[s1++] = arr[i];
    }
    //printf("\n");
}

void mergeSort(int *nums, int start, int end) {
    //printf("MS %d %d\n", start, end);
    int numsSize = end-start;
    if (numsSize <= 1) {
        return;
    } else {
        int mid = start + (numsSize / 2);
        mergeSort(nums, start, mid);
        mergeSort(nums, mid, end);
        merge(nums, start, mid, mid, end);
    }
}

int reversePairs(int *nums, int numsSize) {
    ans = 0;
    mergeSort(nums, 0, numsSize);
    return ans;
}

int main(int argc, char const *argv[])
{
    int arr[] = {2,4,3,5,1};
    // int arr[] = {2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
    int arrSize = 6;
    // for (int i = 0; i < arrSize; ++i)
    // {
    //     //printf("%d ", arr[i]);
    // }
    // //printf("\n");
    printf("%d\n", reversePairs(arr, arrSize));
    return 0;
}
