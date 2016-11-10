// https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/

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

listnode* deleteDuplicates(listnode* A) {
    listnode *unique_list = NULL;
    listnode *unique_list_iter = NULL;
    int last_val = 0;
    while(A!=NULL) {
        if ((A->next !=NULL)
            && (A->val == A->next->val)) {
            last_val = A->val;
            while((A != NULL)
                && (A->val == last_val)) {
                A = A->next;
            }
        } else {
            if (unique_list_iter == NULL) {
                unique_list_iter = listnode_new(A->val);
                unique_list = unique_list_iter;
            } else {
                listnode *new = listnode_new(A->val);
                unique_list_iter->next = new;
                unique_list_iter = new;
            }
            A = A->next;
        }
    }
    return unique_list;
}

int main(int argc, char const *argv[])
{
    listnode *n1 = listnode_new(1);
    listnode *n2 = listnode_new(2);
    listnode *n3 = listnode_new(2);
    listnode *n4 = listnode_new(2);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = NULL;
    listnode *x = deleteDuplicates(n1);
    while(x!=NULL) {
        printf("%d\n", x->val);
        x = x->next;
    }
    return 0;
}
