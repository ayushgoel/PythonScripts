// https://www.interviewbit.com/problems/nqueens/

#include <stdio.h>
#include <stdlib.h>

void print_grid(char **x, int l) {
    printf("PRINTING\n");
    for (int i = 0; i < l; ++i)
    {
        for (int j = 0; j < l; ++j)
        {
            if (x[i][j] == 'Q')
            {
                printf("%c ", x[i][j]);
            } else {
                printf(". ");
            }
        }
        printf("\n");
    }
}

int check_diagnols(char **board, int row, int col, int current_row, int current_col) {
    int i, j;
    for (i = current_row+1, j = current_col+1; i < row && j< col; ++i, ++j) {
        if (board[i][j] == 'Q') {
            return 0;
        }
    }
    for (i = current_row-1, j = current_col-1; i >=0 && j>=0; --i, --j) {
        if (board[i][j] == 'Q') {
            return 0;
        }
    }
    for (i = current_row+1, j = current_col-1; i < row && j>=0; ++i, --j) {
        if (board[i][j] == 'Q') {
            return 0;
        }
    }
    for (i = current_row-1, j = current_col+1; i >=0 && j< col; --i, ++j) {
        if (board[i][j] == 'Q') {
            return 0;
        }
    }
    return 1;
}

int isPartialSolution(char **board, int row, int col) {
    printf("PS being checked %d %d\n", row, col);
    print_grid(board, col);
    int i;
    for (i = 0; i < row; ++i)
    {
        int has_queen = 0;
        int j;
        for (j = 0; j < col; ++j)
        {
            // printf("BOARD element %d %d %c\n", i, j, board[i][j]);
            if (board[i][j] == 'Q')
            {
                has_queen += 1;
                int k;
                // check only queen for column j
                for (k = 0; k < row; ++k)
                {
                    if (board[k][j] == 'Q' && k != i)
                    {
                        printf("FOUND Q at %d %d when should be at %d\n", k, j, i);
                        return 0;
                    }
                }
                // check only Q in diagnol
                int diagnol_check = check_diagnols(board, row, col, i, j);
                if (diagnol_check == 0)
                {
                    printf("Queen on diagnols\n");
                    return 0;
                }
            }
        }
        if (has_queen == 0)
        {
            printf("Don't have queen for %d\n", i);
            return 0;
        }
        if (has_queen > 1)
        {
            printf("More than 1 queen on row %d\n", i);
            return 0;
        }
    }
    return 1;
}

int isSolution(char **board, int l) {
    return isPartialSolution(board, l, l);
}

int solve(char **board, int l, int pos) {
    printf("S %d\n", pos);
    if (pos == l)
    {
        printf("REACHED TO CHECK SOLUTION\n");
        if (isSolution(board, l))
        {
            printf("We have a solution !!! 🎉\n");
            return 1;
        } else {
            printf("Solution discarded\n");
            return 0;
        }
    }
    int i;
    for (i = 0; i < l; ++i)
    {
        printf("SETTING Q at %d %d\n", pos, i);
        board[pos][i] = 'Q';
        if (isPartialSolution(board, pos+1, l))
        {
            printf("Partially correct\n");
            int x = solve(board, l, pos+1);
            if (x == 1)
            {
                return x;
            }
        } else {
            board[pos][i] = '.';
        }
    }
    return 0;
}

char **find_solution(int n, int i) {
    printf("FS %d\n", i);
    char **sol = malloc(n * sizeof(char *));
    int j;
    for (j = 0; j < n; ++j)
    {
        sol[j] = malloc((n+1) * sizeof(char));
        sol[j][n] = '\0';
    }
    int x;
    for (x = 0; x < n; ++x)
    {
        for (j = 0; j < n; ++j)
        {
            sol[x][j] = '.';
        }
    }
    sol[0][i] = 'Q';
    int solved = solve(sol, n, 1);
    if (solved == 1) {
        return sol;
    } else {
        return NULL;
    }
}

/**
 * @input A : Integer
 *
 * @Output 2D string array. You need to malloc memory. Fill in len1 as row, len2 as columns. All strings should end with '\0'.
 * For example, a valid output : [["..Q.","Q...", "...Q", ".Q.." ], [".Q..", "...Q", "Q...", "..Q."]]
 * len1 = 2, len2 = 4.
 */
char*** solveNQueens(int A, int *number_of_solutions, int *size_of_grid) {
    *size_of_grid = A;
    char ***ans = malloc(A * sizeof(char **));
    *number_of_solutions = 0;

    int i;
    for (i = 0; i < A; ++i)
    {
        char **ansi = find_solution(A, i);
        if (ansi != NULL)
        {
            printf("We have a solution!\n");
            ans[*number_of_solutions] = ansi;
            *number_of_solutions = *number_of_solutions + 1;
        }
        printf("SNQ Didn't find a solution\n");
    }
    printf("We did get solutions count %d\n", *number_of_solutions);
    return ans;
}

int main(int argc, char const *argv[])
{
    int number_of_solutions;
    int size_of_grid;
    int size = 5;
    char ***ans = solveNQueens(size, &number_of_solutions, &size_of_grid);
    printf("ANSWER\n");
    for (int i = 0; i < number_of_solutions; ++i)
    {
        for (int j = 0; j < size; ++j)
        {
            for (int k = 0; k < size; ++k)
            {
                printf("%c ", ans[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }

    // char *a[4] = {".Q..", "...Q", "Q...", "..Q."};
    // printf("%d\n", isPartialSolution(a, 4, 4));
    return 0;
}
