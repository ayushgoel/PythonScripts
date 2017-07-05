bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
    int i = 0, j = 0;
    for (i = 1; i< matrixRowSize; ++i) {
        // printf("1. %d\n",  matrix [i][0]);
        if (target < matrix [i][0]) {
            break; // i is the row
        }
    }
    i--;

    for (j = 0; j < matrixColSize; ++j) {
        if (target == matrix[i][j]) {
            return true;
        }
    }
    return false;
}


//Testcases

// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// 3
// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// 30
// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// 50
// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// 1
// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// -1
// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// 52
// [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
// 13