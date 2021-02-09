/***from dust i have come, dust i will be***/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL) return head;
        else if(head->next == NULL) return head;
        
        ListNode *i = head, *j = head->next, *temp;
        while(i != NULL && j != NULL)
        {
            if(i->val == j->val)
                temp = j, j = j->next, i->next = j, delete(temp);
            else
            {
                i = j;
                j = j->next;
            }   
        }
        
        return head;
    }
};
