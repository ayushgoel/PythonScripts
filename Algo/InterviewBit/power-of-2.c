// https://www.interviewbit.com/problems/power-of-2/

#include <stdio.h>
#include <stdlib.h>

int is_even(char c) {
    char even_nums[] = {'2','4','6','8','0'};
    int i;
    for (i = 0; i < 5; ++i)
    {
        if (even_nums[i] == c)
        {
            return 1;
        }
    }
    return 0;
}

int len(char *s) {
    int i;
    for (i = 0; *s != '\0'; ++i, ++s) { }
    return i;
}

int is2(char *s) {
    if (len(s) == 1 && *s == '2')
    {
        return 1;
    }
    return 0;
}

char div_by_2_first_19(char *s) {
    if (*s == '0')
    {
        return '0';
    } else if (*s == '2' || *s == '3')
    {
        return '1';
    } else if (*s == '4' || *s == '5')
    {
        return '2';
    } else if (*s == '6' || *s == '7')
    {
        return '3';
    } else if (*s == '8' || *s == '9')
    {
        return '4';
    } else if (*s == '1') {
        s++;
        if (*s == '0' || *s == '1')
        {
            return '5';
        } else if (*s == '2' || *s == '3')
        {
            return '6';
        } else if (*s == '4' || *s == '5')
        {
            return '7';
        } else if (*s == '6' || *s == '7')
        {
            return '8';
        } else if (*s == '8' || *s == '9')
        {
            return '9';
        }
    }
    printf("ERROR IN DIVINDING %s\n", s);
    return '~';
}

char div_by_2_first_19_remainder(char c) {
    if (is_even(c))
    {
        return '0';
    }
    return '1';
}

char *divide_by_2(char *s) {
    char *ans = malloc(15 * sizeof(char));
    char *ans_iter = ans;
    char remainder = '0';
    char *iter = s;
    for (; *iter != '\0'; ++iter)
    {
        // printf("string: %s iterator: %s ans: %c\n", s, iter, *ans);
        if (remainder == '1')
        {
            // printf("remainder 1\n");
            char *t = malloc(3*sizeof(char));
            *t = '1';
            *(t+1) = *iter;
            *(t+2) = '\0';
            *ans_iter = div_by_2_first_19(t);
            ans_iter++;
            remainder = div_by_2_first_19_remainder(*iter);
            continue;
        }
        if (*iter == '1')
        {
            // printf("iter 1\n");
            char *t = malloc(3*sizeof(char));
            *t = *iter;
            iter++;
            *(t+1) = *iter;
            *(t+2) = '\0';
            *ans_iter = '0';
            ans_iter++;
            *ans_iter = div_by_2_first_19(t);
            ans_iter++;
            remainder = div_by_2_first_19_remainder(*iter);
            continue;
        } else {
            // printf("iter else\n");
            *ans_iter = div_by_2_first_19(iter);
            // printf("Char!%c\n", *ans_iter);
            ans_iter++;
            remainder = div_by_2_first_19_remainder(*iter);
            continue;
        }
    }
    *ans_iter = '\0';
    for (; *ans == '0'; ans++);
    return ans;
}

int power(char* A) {
    if (is2(A))
    {
        return 1;
    }
    int i;
    char *iter;
    char last_char;
    for (iter = A; *iter != '\0'; iter++)
    {
        last_char = *iter;
    }
    if (is_even(last_char) == 0)
    {
        return 0;
    }
    char *divided_by_two = divide_by_2(A);
    // printf("last char: %c iseven? %d %s\n", last_char, is_even(last_char), divided_by_two);
    return power(divided_by_two);
}

int main(int argc, char const *argv[])
{
    char *num = "147573952589676412928";
    printf("2^k? %d\n", power(num));
    return 0;
}
