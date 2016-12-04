// https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/

#include <stdio.h>
#include <stdlib.h>

// Definition for binary tree
struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

typedef struct TreeNode treenode;

treenode *treenode_new(int val) {
  treenode* node = (treenode *)malloc(sizeof(treenode));
  node->val = val;
  node->left = NULL;
  node->right = NULL;
  return node;
}

struct MyNode {
  int val1;
  int val2;
  struct MyNode *left;
  struct MyNode *right;
};

typedef struct MyNode mynode;

mynode *mynode_new(int val1, int val2) {
  mynode* node = (mynode *)malloc(sizeof(mynode));

  // This value is the maximum sum attained by extending either the left or right subtree
  // (or by not extending at all). Thus when dp is calculating the max, it can use this
  // value to extend it's path.
  node->val1 = val1;

  // This value keeps track of the path that can be created by adjoining the left and right
  // subtree.
  node->val2 = val2;

  node->left = NULL;
  node->right = NULL;
  return node;
}

int max(int a, int b) {
    return a>b ? a : b;
}

mynode * fillDP(treenode *t) {
    if (t == NULL)
    {
        return NULL;
    }
    mynode *leftDP = fillDP(t->left);
    mynode *rightDP = fillDP(t->right);

    mynode *n = mynode_new(t->val, t->val);
    if (leftDP != NULL && rightDP != NULL)
    {
        int v = max(0, (max(leftDP ->val1, rightDP -> val1))); // Extend left/right or do not use any and create new path(0).
        n->val1 += v;
        n->val2 += leftDP->val1 + rightDP->val1; // Join left and right subtree.
    } else if (leftDP != NULL)
    {
        n->val1 += max(0, leftDP->val1);
        n->val2 += leftDP->val1;
    } else if (rightDP != NULL)
    {
        n->val1 += max(0, rightDP->val1);
        n->val2 += rightDP->val1;
    }
    n->left = leftDP;
    n->right = rightDP;
    return n;
}

int findMaxInTree(mynode *t) { // when extending child
    if (t->left != NULL)
    {
        int leftMax = findMaxInTree(t->left);
        if (t->right != NULL)
        {
            int rightMax = findMaxInTree(t->right);
            return max(t->val2, max(t->val1, max(leftMax, rightMax))); // Maximum of left subtree, right subtree and own's val1 and val2.
        }
        return max(t->val2, max(t->val1, leftMax));
    } else if (t->right != NULL)
    {
        int rightMax = findMaxInTree(t->right);
        return max(t->val2, max(t->val1, rightMax));
    }
    return max(t->val2, t->val1);
}

/**
 * @input A : Root pointer of the tree
 *
 * @Output Integer max sum on path
 */
int maxPathSum(treenode* a) {
    mynode *dp = fillDP(a);
    return findMaxInTree(dp);
}

int main(int argc, char const *argv[])
{
    treenode *n2 = treenode_new(-2);
    treenode *n3 = treenode_new(3);
    treenode *n4 = treenode_new(-4);
    treenode *n1 = treenode_new(-1);

    n2->left = n1;
    n2->right = n3;
    n3->right = n4;
    printf("%d\n", maxPathSum(n2));
    return 0;
}