#include<stdio.h>

int reversePairs(int* nums, int numsSize) {
    int ans=0;
    for(int i =1; i< numsSize; ++i) {
        for(int j=i-1;j>=0;--j) {
            // printf("%d %d %d %d %d\n", nums[j], nums[i], j, i, ans);
            if((nums[j]>>1 > nums[i])
               || ((nums[j]>>1 == nums[i]) && nums[j]%2==1)) {
                ans++;
            } else {
                break;
            }
        }
        while(i>0 && nums[i] < nums[i-1]) {
            int t = nums[i];
            nums[i] = nums[i-1];
            nums[i-1] = t;
            --i;
        }
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int arr[] = {1,2,3,2,1};
    printf("%d\n", reversePairs(arr, 5));
    return 0;
}