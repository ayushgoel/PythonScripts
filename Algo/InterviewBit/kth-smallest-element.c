// https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Memory Limit Exceeded

// /**
//  * @input A : Read only ( DON'T MODIFY ) Integer array
//  * @input n1 : Integer array's ( A ) length
//  * @input B : Integer
//  *
//  * @Output Integer
//  */
// int kthsmallest(const int* A, int n1, int k) {
//     int *b = malloc(n1 * sizeof(int));
//     int *c = malloc(n1 * sizeof(int));
//     int i ,j=0, l=0;
//     int kthelement = A[k-1];
//     for (i = 0; i < n1; ++i) {
//         if (i == k-1) {
//             continue;
//         }
//         if (A[i] <= kthelement) {
//             b[j++] = A[i];
//         } else {
//             c[l++] = A[i];
//         }
//     }
//     if (j == k) {
//         return kthelement;
//     } else if (j > k) {
//         return kthsmallest(b, j, k);
//     } else { // j<k
//         return kthsmallest(c, l, k-j);
//     }
// }

// Can't modify array

// /**
//  * @input A : Read only ( DON'T MODIFY ) Integer array
//  * @input n1 : Integer array's ( A ) length
//  * @input B : Integer
//  *
//  * @Output Integer
//  */
// int kthsmallest(const int* A, int n1, int k) {
//     int kthelementindex = 0;
//     int i;
//     for (i = 1; i < k; ++i) {
//         if (A[i] > A[kthelementindex]) {
//             kthelementindex = i;
//         }
//     }
//     for (; i < n1; ++i) {
//         if (A[i] < A[kthelementindex]) {
//             A[kthelementindex] = -1;
//             int j;
//             kthelementindex = 0;
//             for (j = 0; j <= i; ++j) {
//                 if (A[j] > A[kthelementindex]) {
//                     kthelementindex = j;
//                 }
//             }
//         }
//     }
//     return A[kthelementindex];
// }


// Does not work with duplicates

// /**
//  * @input A : Read only ( DON'T MODIFY ) Integer array
//  * @input n1 : Integer array's ( A ) length
//  * @input B : Integer
//  *
//  * @Output Integer
//  */
// int kthsmallest(const int* A, int n1, int k) {
//     int * klist = malloc((k-1) * sizeof(int));
//     int kthelementindex = 0;
//     int i;
//     for (i = 0; i < k; ++i) {
//         klist[i] = A[i];
//         if (A[i] > A[kthelementindex]) {
//             kthelementindex = i;
//         }
//     }
//     for (; i < n1; ++i) {
//         if (A[i] < A[kthelementindex]) {
//             klist[kthelementindex] = A[i];
//             kthelementindex = 0;
//             int j;
//             for (j = 1; j < k; ++j) {
//                 if (klist[j] > klist[kthelementindex]) {
//                     kthelementindex = j;
//                 }
//             }
//         }
//     }
//     return klist[kthelementindex];
// }

// Uses extra space

// /**
//  * @input A : Read only ( DON'T MODIFY ) Integer array
//  * @input n1 : Integer array's ( A ) length
//  * @input B : Integer
//  *
//  * @Output Integer
//  */
// int min_element_index(const int* A, int n1) {
//     int i, min_index = 0;
//     for (i = 1; i < n1; ++i) {
//         if (A[i]<A[min_index]) {
//             min_index = i;
//         }
//     }
//     return min_index;
// }

// int kthsmallest(const int* A, int n1, int k) {
//     int *klist = malloc(n1 * sizeof(int));
//     int i = 0;
//     for (i = 0; i < n1; ++i)
//     {
//         klist[i] = A[i];
//     }
//     int len = n1;
//     for (i = 0; i < (k-1); ++i)
//     {
//         int min_index = min_element_index(klist, n1-i);
//         int tmp = klist[min_index];
//         // printf("%d %d %d %d\n", i, min_index, tmp, klist[0]);

//         // int t;
//         // for (t = 0; t < n1-i; ++t)
//         // {
//         //     printf("%d ", klist[t]);
//         // }
//         // printf("\n");

//         klist[min_index] = klist[0];
//         // klist[i] = tmp;
//         klist++;
//     }
//     return klist[min_element_index(klist, n1-i)];
// }

int mod(int n) {
    return (n>0) ? n : -n;
}

int kthsmallest(const int* A, int n1, int k) {
    int l=0, u=INT_MAX;
    while(1) {
        int m = (l+u)/2;
        int less_elements = 0, equal_elements = 0, least_max_element = 0;
        int i;
        for (i = 0; i < n1; ++i) { // Find less and equal elements from current middle element `m`
            if (A[i] < m) {
                less_elements++;
                if (A[i] > least_max_element) {
                    least_max_element = A[i];
                }
            } else if (A[i] == m) {
                equal_elements++;
            }
        }

        // printf("%d %d %d %d %d %d \n", l,m,u, k, less_elements, equal_elements);

        if (less_elements == k && (mod(least_max_element - m) < 100)) { // `m` has k less elements than it ) { // `m` has (less than k) less elements and
            m--; // the kth element will have k-1 elements less than it.
            while(1) {
                int i;
                for (i = 0; i < n1; ++i) {
                    if (A[i] == m) {
                        return m;
                    }
                }
                if (less_elements == 0) {
                    m++;
                } else {
                    m--;
                }
            }
        }
        if ((less_elements < k && (less_elements + equal_elements) >= k)) {
            return m;
        }
        if (less_elements < k) {
            l = m;
        } else {
            u = m;
        }
    }
}

int main(int argc, char const *argv[]) {
    // int len = 2;
    // int k = 2;
    // const int a[2] = { 94, 87, 100, 11, 23, 98, 17, 35, 43, 66, 34, 53, 72, 80, 5, 34, 64, 71, 9, 16, 41, 66, 96 };
    // { 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 };
    // { 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 };
    // { 60, 94, 63, 3, 86, 40, 93, 36, 56, 48, 17, 10, 23, 43, 77, 1, 1, 93, 79, 4, 10, 47, 1, 99, 91, 53, 99, 18, 52, 61, 84, 10, 13, 52, 3, 9, 78, 16, 7, 62 };

    int len = 2;
    int k = 2;
    const int a[2] = {47,7};
    int expected_answer = 47;

    // int len = 19;
    // int k = 6;
    // const int a[19] = {44, 69, 63, 90, 69, 83, 48, 87, 99, 63, 45, 26, 82, 35, 37, 4, 97, 29, 91};
    // int expected_answer = 44;

    //printf("%d\n", kthsmallest(a, 46, 9));
    printf("%d expected: %d\n", kthsmallest(a, len, k), expected_answer);
    return 0;
}
