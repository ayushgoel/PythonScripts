#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// #define true 1
// #define false 0
// #define bool int

bool increasingTriplet(int* a, int numsSize) {
    if (numsSize < 3) {
        return false;
    }
    bool isAvail[3] = {false,false,false};
    int arr[3] = {0,0,0};
    for (int i = 0; i < numsSize; ++i) {
        printf("%d %d %d %d %d %d %d\n", a[i], isAvail[0], arr[0], isAvail[1], arr[1], isAvail[2], arr[2]);
        if (isAvail[0] == false) {
            arr[0] = a[i];
            isAvail[0] = true;
        } else {
            if (arr[0] < a[i]) {
                if (isAvail[1] == true) {
                    if (arr[1] < a[i])
                    {
                        return true;
                    } else {
                        arr[1] = a[i];
                    }
                } else {
                    arr[1] = a[i];
                    isAvail[1] = true;
                }
            } else {
                if (isAvail[2] == true) {
                    //ai is smaller than arr0 and we have arr2
                    if (isAvail[1] == false) {
                        if (a[i] > arr[2]) {
                            // printf("Q%d %d %d %d %d %d %d\n", a[i], isAvail[0], arr[0], isAvail[1], arr[1], isAvail[2], arr[2]);
                            arr[0] = arr[2];
                            arr[1] = a[i];
                            isAvail[1] = true;
                            isAvail[2] = false;
                        } else {
                            arr[0] = arr[2];
                            arr[2] = a[i];
                        }
                    } else {
                        if (arr[2] < a[i]) {
                            if (a[i] < arr[1]) {
                                arr[0] = arr[2];
                                arr[1] = a[i];
                                arr[2] = 0;
                                isAvail[2] = false;
                            } else {
                            printf("T%d %d %d %d %d %d %d\n", a[i], isAvail[0], arr[0], isAvail[1], arr[1], isAvail[2], arr[2]);
                                printf("NOT POSSIBLE\n");
                                continue;
                            }
                        } else {
                            arr[2] = a[i];
                        }
                    }
                } else {
                    arr[2] = a[i];
                    isAvail[2] = true;
                }
            }
        }
        // arr[0] is first element
        // arr[1] is second element
        // arr[2] is possible first element since lower than arr[0]
        // isAvail[3] to know how much found
        // if isAvail[0] not set, set to arr[0]
        // isAvail[0] set,
        //          if isAvail[1] set, a[i] > arr[1] continue
        //                            else if a[i] > arr[0] set to arr[1]
        //                            else if isAvail[2] set, if a[i] > arr[2] set to arr[0] and arr[1] and reset arr[2]
        //                                                    else set to arr[2]
        //                                 else if a[i] >
    }
    return false;
}

int main(int argc, char const *argv[])
{
    // int a[] = {1, 2, 3, 4, 5};
    // int a[] = {5,4,3,2,1};
    // int a[] = {1,2,-10,-8,-7};
    // int a[] = {5,1,5,5,2,5,4};
    int a[] = {1,0,0,1};
    printf("%d\n", increasingTriplet(a, 4));
    return 0;
}