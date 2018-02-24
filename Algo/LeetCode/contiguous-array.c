int findMaxLength(int* nums, int numsSize) {
    if(numsSize <= 1) {
        return 0;
    }
    int *t0=malloc(numsSize * sizeof(int));
    int *t1=malloc(numsSize * sizeof(int));
    int *maxl=malloc(numsSize * sizeof(int));

    if(nums[0] == 0) {
        t0[0] = 1;
        t1[0] = 0;
        maxl[0] = 0;
    } else {
        t0[0] = 0;
        t1[0] = 1;
        maxl[0] = 0;
    }

    for(int i=1; i<numsSize; ++i) {
        if(nums[i] == 0) {
            t0[i] = t0[i-1] + 1;
            t1[i] = t1[i-1];
        } else {
            t0[i] = t0[i-1];
            t1[i] = t1[i-1] + 1;
        }
        // calculate maxl
        maxl[i] = -1;
        if(t0[i] == t1[i]) {
            maxl[i] = i+1;
        } else {
            for(int j = 0; j<i; ++j) {
                if((t0[i]-t0[j]) == (t1[i]-t1[j])) {
                    maxl[i] = i-j;
                    break;
                }
            }
        }
    }

    int ans=0;
    for(int i=1; i<numsSize; ++i) {
        if(maxl[i] > ans) {
            ans = maxl[i];
        }
    }
    return ans;
}