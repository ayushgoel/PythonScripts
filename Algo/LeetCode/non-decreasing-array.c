#include <stdlib.h>
#include <stdio.h>

#define bool int

bool checkPossibility(int* n, int ns) {
    int*q = malloc(ns*sizeof(int));
    for(int i = 0; i<ns; ++i) {
        q[i] = n[i];
    }
    int t=0;
    for(int i=2; i<ns; ++i) {
        if(q[i-1]<q[i-2]){
            if(q[i]>= q[i-2]){
                q[i-1]=q[i-2];
                t++;
            } else {
                t+=2;
                break;
            }
        }
    }
    if(ns>=2 && n[ns-1]<n[ns-2]) {
        t++;
    }
    int u=0;
    for(int i=ns-3; i>=0; --i) {
        if(n[i+1]>n[i+2]){
            if(n[i]<= n[i+2]){
                n[i+1]=n[i+2];
                u++;
            } else {
                u+=2;
                break;
            }
        }
    }
    if(ns>=2 && n[0]>n[1]) {
        u++;
    }
    printf("%d %d\n",t,u);
    return (t<=1 || u<=1);
}

int main(int argc, char const *argv[])
{
    int a[] = {1,3,2,5,4};
    printf("%d\n", checkPossibility(a, 5));
    return 0;
}