// https://www.interviewbit.com/problems/subtract/

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
 * @Output head pointer of list.
 */
listnode* subtract(listnode* A) {
    //reach center, reverse second half
    listnode *half = A, *fast_iter = A;
    while(fast_iter!=NULL && fast_iter->next!=NULL) {
        half = half->next;
        fast_iter = fast_iter->next->next;
    }
    // printf("1 %d\n", half->val);

    listnode *reverse_iter = half;
    listnode *reverse_next = half->next;
    while(reverse_next != NULL) {
        listnode *t = reverse_next->next;
        reverse_next->next = reverse_iter;
        reverse_iter = reverse_next;
        reverse_next = t;
    }
    // printf("2 %d\n", reverse_iter->val);

    //do subtraction
    listnode *iter = A;
    listnode *iter_reverse = reverse_iter;
    while(iter != half) {
        iter->val = iter_reverse->val - iter->val;
        iter = iter->next;
        iter_reverse = iter_reverse->next;
    }
    // printf("3 %d %d %d\n", iter_reverse->val, half->val, iter->val);

    // listnode *x = reverse_iter;
    // while(x!=NULL) {
    //     printf("X %d\n", x->val);
    //     x = x->next;
    // }

    //reverse second half again
    listnode *reverse_iter2 = reverse_iter;
    listnode *reverse_next2 = reverse_iter->next;
    while(reverse_iter2 != half) {
        // printf("Ex %d %d\n", reverse_next2->val, reverse_iter2->val);
        listnode *t = reverse_next2->next;
        reverse_next2->next = reverse_iter2;
        reverse_iter2 = reverse_next2;
        reverse_next2 = t;
    }
    reverse_iter->next = NULL;

    //printf("4 %d %d\n", reverse_iter2->val, reverse_next2->val);
    return A;
}


int main(int argc, char const *argv[])
{
    listnode *n1 = listnode_new(1);
    listnode *n2 = listnode_new(2);
    listnode *n3 = listnode_new(3);
    listnode *n4 = listnode_new(40);
    listnode *n5 = listnode_new(50);
    listnode *n6 = listnode_new(60);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n5;
    n5->next = n6;
    n6->next = NULL;

    listnode *x = subtract(n1);
    while(x!=NULL) {
        printf("X %d\n", x->val);
        x = x->next;
    }
    return 0;
}


