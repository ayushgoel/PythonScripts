// https://www.interviewbit.com/problems/reverse-link-list-ii/

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
 int val;
 struct ListNode *next;
};

typedef struct ListNode listnode;

listnode* listnode_new(int val) {
 listnode* node = (listnode *) malloc(sizeof(listnode));
 node->val = val;
 node->next = NULL;
 return node;
}

/**
 * @input A : Head pointer of linked list
 * @input m : Integer
 * @input n : Integer
 *
 * @Output head pointer of list.
 */
listnode* reverseBetween(listnode* A, int m, int n) {
    int index = 1;
    listnode *n1 = A;
    listnode *n2 = A;

    listnode *iter = A;
    listnode *change_node = A;
    listnode *prev = NULL;
    int reverse = 0;
    while(iter!=NULL) {
        printf("%d %d\n", iter->val, index);
        if (index == m-1)
        {
            printf("1\n");
            n1 = iter;
        }
        if (index == m)
        {
            printf("2\n");
            n2 = iter;
        }
        if (index == n)
        {
            printf("3\n");
            if (m == 1)
            {
                A = iter;
            } else {
                n1->next = iter;
            }
        }
        if (index == n+1)
        {
            printf("4\n");
            n2->next = iter;
        }
        if (index >= m && index <= n)
        {
            printf("5\n");
            change_node = iter;
            iter = iter->next;
            change_node->next = prev;
            prev = change_node;
        } else {
            printf("6\n");
            prev = iter;
            iter = iter->next;
        }
        ++index;
    }
    if (index == n+1)
    {
        n2->next = iter;
    }

    return A;
}

int main(int argc, char const *argv[])
{
    listnode *n1 = listnode_new(1);
    listnode *n2 = listnode_new(2);
    listnode *n3 = listnode_new(3);
    listnode *n4 = listnode_new(4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = NULL;

    listnode *x = reverseBetween(n1, 1, 4);
    while(x!=NULL) {
        printf("X %d\n", x->val);
        x = x->next;
    }
    return 0;
}

