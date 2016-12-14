// https://www.interviewbit.com/problems/length-of-last-word/

#include <stdio.h>

/**
 * @input A : Read only ( DON'T MODIFY ) String termination by '\0'
 *
 * @Output Integer
 */
int lengthOfLastWord(const char* s) {
    int i;
    int cnt = 0;
    int last_char_was_space = 1;
    for (i = 0; s[i] != '\0'; ++i)
    {
        // printf("%c\n", s[i]);
        if (s[i] == ' ')
        {
            last_char_was_space = 1;
        } else {
            if (last_char_was_space == 1)
            {
                cnt = 0;
                last_char_was_space = 0;
                // printf("done 0\n");
            }
            cnt++;
            // printf("increased\n");
        }
    }
    return cnt;
}

int main(int argc, char const *argv[])
{
    printf("%d \n", lengthOfLastWord(" af sfd "));
    return 0;
}