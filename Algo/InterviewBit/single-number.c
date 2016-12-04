/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int singleNumber(const int* a, int n) {
    int i;
    int ans = a[0];
    for(i=1; i<n; ++i) {
        ans = ans ^ a[i];
    }
    return ans;
}
