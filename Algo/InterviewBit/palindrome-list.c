// https://www.interviewbit.com/problems/palindrome-list/

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
 *
 * @Output Integer
 */

listnode *reverse_list(listnode *n) {
    listnode *t = NULL;
    while(n!= NULL) {
        // printf("X %d\n", n->val);
        listnode *i = n->next;
        n->next = t;
        t = n;
        n = i;
    }
    return t;
}

int compare(listnode *n1, listnode *n2) {
    while (n1 != NULL && n2 != NULL) {
        // printf("%d %d\n", n1->val, n2->val);
        if (n1->val != n2->val)
        {
            return 0;
        }
        n1 = n1->next;
        n2 = n2->next;
    }
    return 1;
}

int lPalin(listnode* A) {
    listnode *ptr1 = A;
    // printf("1\n");

    int len = 0;
    while(ptr1 != NULL) {
        ptr1 = ptr1->next;
        ++len;
    }
    // printf("2\n");

    ptr1 = A;
    listnode *ptr2 = A;
    while(ptr2->next != NULL && ptr2->next->next != NULL) {
        // printf("3\n");
        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;
        // printf("3.1\n");
    }
    // printf("3.x\n");

    listnode *rptr = reverse_list(ptr1->next);
    // printf("4\n");
    // printf("4 %d\n", rptr->val);
    // printf("4 %d %d\n", rptr->val, rptr->next->val);

    return compare(A, rptr);
}

int main(int argc, char const *argv[])
{
    listnode *n1 = listnode_new(1);
    listnode *n2 = listnode_new(2);
    listnode *n3 = listnode_new(2);
    listnode *n4 = listnode_new(1);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = NULL;
    printf("%d\n", lPalin(n1));
    return 0;
}
