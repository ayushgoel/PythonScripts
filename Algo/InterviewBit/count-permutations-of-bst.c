// https://www.interviewbit.com/problems/count-permutations-of-bst/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Integer
 * @input B : Integer
 *
 * @Output Integer
 */

int answer(int numbers, int height, int max_element_level, int ***dp) {
    printf("D %d %d %d\n", numbers, height, max_element_level);
    if (numbers <= 0
        || height <= 0
        || max_element_level < 0
        || max_element_level > height) {
        return 0;
    }
    if (numbers == 1)
    {
        return 1;
    }

    if (dp[numbers][height][max_element_level] != 0)
    {
        return dp[numbers][height][max_element_level];
    }

    if (max_element_level == 0)
    {

    }

    int i;
    int ans = 0;
    ans += answer(numbers - 1, height - 1, max_element_level - 1, dp);
    for (i = 1; i < max_element_level; ++i)
    {
        ans += answer(numbers - 1, height, i, dp);
    }
    dp[numbers][height][max_element_level] = ans;
    return ans;
}

int cntPermBST(int A, int B) {
    int ldp = 1000;
    printf("X\n");
    int ***dp = malloc(ldp*ldp*ldp * sizeof(int));
    printf("Y\n");
    int i;
    for (int i = 0; i < ldp; ++i)
    {
        dp[i] = malloc(ldp * sizeof(int *));
        int j;
        for (j = 0; j < ldp; ++j)
        {
            dp[i][j] = malloc(ldp * sizeof(int));
        }
    }

    printf("REached\n");
    int ans = 0;
    for (i = 0; i < B; ++i)
    {
        ans += answer(A, B, i, dp);
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    printf("XX\n");
    printf("%d\n", cntPermBST(3, 1));
    return 0;
}
