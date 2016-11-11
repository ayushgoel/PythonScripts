// https://www.interviewbit.com/problems/redundant-braces/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : String termination by '\0'
 *
 * @Output Integer
 */
int braces(char* A) {
    int len = 0;
    for (; A[len]!='\0'; ++len) { }

    char *stack = malloc(len * sizeof(int));

    int i;
    int index = 0;
    for (i = 0; A[i] != '\0'; ++i)
    {
        if (A[i] == ')') {
            int count = 0;
            index--; // we are on pushing position
            while (stack[index] != '(') {
                if (stack[index] == '+'
                    || stack[index] == '-'
                    || stack[index] == '*'
                    || stack[index] == '/')
                {
                    ++count;
                }
                index--;
            }
            if (count == 0)
            {
                return 1;
            }
        } else {
            stack[index++] = A[i];
        }
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    char *s = "((a+b))";
    printf("%d\n", braces(s));
    return 0;
}
