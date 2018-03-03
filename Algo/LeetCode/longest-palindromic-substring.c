#include <stdio.h>
#include <stdlib.h>

int dp[1001][1001];

int getPalindromeLength(char *s, int i, int j) {
    // printf("%d %d\n", i, j);
    if(dp[i][j] != -1) {
        return dp[i][j];
    }
    if(i == j) {
        dp[i][j] = 1;
    } else if(s[i] == s[j]) {
        if(i+1 == j) {
            dp[i][j] = 2;
        } else {
            int lesserLength = getPalindromeLength(s, i+1, j-1);
            if(lesserLength != 0) {
                dp[i][j] = lesserLength + 2;
            } else {
                dp[i][j] = 0;
            }
        }
    } else {
        dp[i][j] = 0;
    }
    return dp[i][j];
}

char* longestPalindrome(char* s) {
    int slen = 0;
    for(;s[slen]!= '\0';++slen);

    for(int i = 0; i<slen; ++i) {
        for (int j=0; j<slen; ++j) {
            dp[i][j] = -1;
        }
    }

    int maxi = -1;
    int maxj = -1;
    for(int i=0; i < slen; ++i) {
        for(int j=i; j < slen; ++j) {
            getPalindromeLength(s, i, j);
            if(dp[i][j] > (maxj - maxi)) {
                maxi = i;
                maxj = j;
            }
        }
    }

    // for(int i=0; i < slen; ++i) {
    //     for(int j=i; j < slen; ++j) {
    //         if(dp[i][j] > (maxj - maxi)) {
    //             maxi = i;
    //             maxj = j;
    //         }
    //     }
    // }

    char *ans = malloc((maxj-maxi+2) * sizeof(char));
    int i,k;
    for(i = maxi, k = 0; i <= maxj; ++i, ++k) {
        ans[k] = s[i];
    }
    ans[k] = '\0';
    return ans;
}

int main(int argc, char const *argv[])
{
    printf("%s\n", longestPalindrome("abcdasdfghjkldcba"));
    printf("%s\n", longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"));
    return 0;
}