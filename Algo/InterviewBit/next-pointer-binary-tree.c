// https://www.interviewbit.com/problems/next-pointer-binary-tree/

#include <stdio.h>
#include <stdlib.h>

// *
//  * Definition for binary tree
//  *
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left, *right, *next;
};
typedef struct TreeLinkNode treelinknode;

treelinknode *newNode(int val) {
    treelinknode *n = malloc(sizeof(treelinknode));
    n->val = val;
    n->left = NULL;
    n->right = NULL;
    return n;
}

treelinknode *findNextLeft(treelinknode *a) {
    if (a == NULL) {
        return NULL;
    }
    treelinknode *x = a->next;
    // printf("FN\n");
    while(x != NULL) {
        // printf("FN %d\n", x->val);
        if (x->left != NULL) {
            return x->left;
        }
        if (x->right != NULL) {
            return x->right;
        }
        x = x->next;
    }
    // printf("Returning NULL\n");
    return NULL;
}
/**
 * @input A : Root pointer of the tree
 *
 * @Output Void. Just modifies the args passed by reference
 */
void connect(treelinknode* a) {
    a->next = NULL;
    treelinknode *cur, *next;
    cur = a;
    next = NULL;

    while(1) {
        if (cur == NULL) {
            // printf("cur is NULL \n");
            if (next == NULL) {
                // printf("Breaking\n");
                break;
            } else {
                // printf("Next is not NULL\n");
                cur = next;
                next = NULL;
            }
        }
        // printf("X %d %d %d\n", cur->val, cur->left->val, cur->right->val);
        if (next == NULL) {
            if (cur->left != NULL) {
                next = cur->left;
            } else {
                next = cur->right;
            }
        }
        if (cur->left != NULL) {
            if (cur->right != NULL) {
                cur->left->next = cur->right;
                // printf("Set left next %d %d\n", cur->left->val, cur->right->val);
            } else {
                cur->left->next = findNextLeft(cur);
                // printf("No right %d\n", cur->left->next->val);
            }
        }
        if (cur->right != NULL) {
            // printf("Finding for right %d\n", cur->val);
            cur->right->next = findNextLeft(cur);
        }
        cur = cur->next;
    }
}

void printTree(treelinknode *node) {
    printf("Printing\n");
    if (node == NULL)
    {
        printf("NULL\n");
        return;
    }
    printf("L %d\n", node->val);
    printTree(node->left);
    printTree(node->right);
}

int main(int argc, char const *argv[])
{
    treelinknode *root = newNode(2);
    treelinknode *l = newNode(1);
    treelinknode *r = newNode(3);
    root->left = l;
    root->right = r;
    connect(root);
    printTree(root);

    return 0;
}
