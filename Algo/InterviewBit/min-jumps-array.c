// https://www.interviewbit.com/problems/min-jumps-array/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


// /**
//  * @input A : Integer array
//  * @input n1 : Integer array's ( A ) length
//  *
//  * @Output Integer
//  */
// int jump(int* a, int n) {
//     // if (a[0] == 0 && n > 1)
//     // {
//     //     return -1;
//     // }
//     int *min_steps = malloc(n * sizeof(int));
//     int i;
//     for (i = 0; i < n; ++i)
//     {
//         min_steps[i] = INT_MAX;
//     }
//     min_steps[0] = 0;
//     for (i = 0; i < n; ++i)
//     {
//         if (min_steps[i] != INT_MAX)
//         {
//             int j;
//             for (j = 1; j <= a[i] && (i+j < n); ++j)
//             {
//                 if (min_steps[i] + 1 < min_steps[i+j])
//                 {
//                     min_steps[i+j] = min_steps[i] + 1;
//                 }
//             }
//         }
//     }
//     // for (i = 0; i < n; ++i)
//     // {
//     //     printf("%d ", min_steps[i]);
//     // }
//     if (min_steps[n-1] == INT_MAX)
//     {
//         return -1;
//     }
//     return min_steps[n-1];
// }


/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int jump(int* a, int n) {
    int current = 0;
    int max_reached = 0;
    int steps = 0;
    while(1) {
        // printf("%d %d %d\n", current, max_reached, steps);
        if (max_reached >= n-1)
        {
            return steps;
        }
        int i;
        int new_max_reached = 0;
        for (i = current; i <= max_reached; ++i)
        {
            if (i + a[i] > new_max_reached)
            {
                new_max_reached = i + a[i];
            }
        }
        if (new_max_reached == max_reached)
        {
            break;
        }
        current = max_reached + 1;
        max_reached = new_max_reached;
        steps++;
    }
    return -1;
}

int main(int argc, char const *argv[])
{
    printf("%d\n", INT_MAX);
    int in[] = {0, 46, 46, 0, 2, 47, 1, 24, 45, 0, 0, 24, 18, 29, 27, 11, 0, 0, 40, 12, 4, 0, 0, 0, 49, 42, 13, 5, 12, 45, 10, 0, 29, 11, 22, 15, 17, 41, 34, 23, 11, 35, 0, 18, 47, 0, 38, 37, 3, 37, 0, 43, 50, 0, 25, 12, 0, 38, 28, 37, 5, 4, 12, 23, 31, 9, 26, 19, 11, 21, 0, 0, 40, 18, 44, 0, 0, 0, 0, 30, 26, 37, 0, 26, 39, 10, 1, 0, 0, 3, 50, 46, 1, 38, 38, 7, 6, 38, 27, 7, 25, 30, 0, 0, 36, 37, 6, 39, 40, 32, 41, 12, 3, 44, 44, 39, 2, 26, 40, 36, 35, 21, 14, 41, 48, 50, 21, 0, 0, 23, 49, 21, 11, 27, 40, 47, 49};
    int length = 137;
    // int in[]= { 2,3,1,1,4};
    // int length = 5; // 2
    // int in[]= {1,1,1,0,0};
    // int length = 5; // -1
    printf("%d\n", jump(in, length));
    return 0;
}
