//https://leetcode.com/problems/add-two-numbers/

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

// struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
//     struct ListNode *l3 = malloc(sizeof(struct ListNode ));
//     int carry = 0;
//     struct ListNode *tmp = l3;
//     struct ListNode *tmp1;
//     while(l1 != NULL && l2 != NULL) {
//         int val = l1->val + l2->val + carry;
//         carry = val / 10;
//         tmp->val = val % 10;
//         l1 = l1->next;
//         l2 = l2->next;
//         if (l1 != NULL || l2 != NULL) {
//             tmp1 = malloc(sizeof(struct ListNode ));
//             tmp1->next = NULL;
//             tmp->next = tmp1;
//             tmp = tmp1;
//         }
//     }
//     while(l1 != NULL) {
//         int val = l1->val + carry;
//         carry = val / 10;
//         tmp->val = val % 10;
//         l1 = l1->next;
//         if (l1 != NULL) {
//             tmp1 = malloc(sizeof(struct ListNode));
//             tmp1->next = NULL;
//             tmp->next = tmp1;
//             tmp = tmp1;
//         }
//     }
//     while(l2 != NULL) {
//         int val = l2->val + carry;
//         carry = val / 10;
//         tmp->val = val % 10;
//         l2 = l2->next;
//         if (l2 != NULL) {
//             tmp1 = malloc(sizeof(struct ListNode ));
//             tmp1->next = NULL;
//             tmp->next = tmp1;
//             tmp = tmp1;
//         }
//     }
//     if (carry != 0) {
//         tmp1 = malloc(sizeof(struct ListNode ));
//         tmp1->next = NULL;
//         tmp1->val = 1;
//         tmp->next = tmp1;
//     }
//     return l3;
// }

struct ListNode *newNode(int val) {
    struct ListNode *n = malloc(sizeof(struct ListNode));
    n->val = val;
    n->next = NULL;
    return n;
};

struct ListNode* addTwoNumbersWithCarry(struct ListNode* l1, struct ListNode* l2, int carry) {
    if (l1 == NULL && l2 == NULL && carry == 1) {
        return newNode(carry);
    }

    if (l1 == NULL && l2 == NULL && carry == 0) {
        return NULL;
    }

    int v1 = (l1 != NULL) ? l1->val : 0;
    int v2 = (l2 != NULL) ? l2->val : 0;
    int newVal = v1 + v2 + carry;
    int finalVal = newVal % 10;
    int finalCarry = newVal / 10;

    struct ListNode *node = newNode(finalVal);
    struct ListNode *n1 = (l1 != NULL) ? l1->next : NULL;
    struct ListNode *n2 = (l2 != NULL) ? l2->next : NULL;
    node->next = addTwoNumbersWithCarry(n1, n2, finalCarry);

    return node;
}


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    return addTwoNumbersWithCarry(l1, l2, 0);
}

int main() {
    struct ListNode *x1 = malloc(sizeof(struct ListNode ));
    x1->val = 0;
    x1->next = NULL;
    struct ListNode *x2 = malloc(sizeof(struct ListNode));
    x2->val = 1;
    x2->next = NULL;
    struct ListNode *res = addTwoNumbers(x1, x2);
    printf("%d %d", res->val, res->next);
  return 0;
}
