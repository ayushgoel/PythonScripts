/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isValidBSTHL(struct TreeNode* root, int *low, int *high) {
    if (root == NULL) {
        return true;
    }
    if (low != NULL && root->val <= *low) {
        return false;
    }
    if (high != NULL && root->val >= *high) {
        return false;
    }
    int *x = malloc(sizeof(int));
    *x = root->val;
    return (isValidBSTHL(root->left, low, x)
           && isValidBSTHL(root->right, x, high));
}


bool isValidBST(struct TreeNode* root) {
    return isValidBSTHL(root, NULL, NULL);
}