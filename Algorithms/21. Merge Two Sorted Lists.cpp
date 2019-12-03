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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *ans = NULL, *prev = NULL, *curr = NULL;
        while(l1 || l2)
        {
            if(ans == NULL)
            {
                if(l1 && l2){
                    if(l1->val < l2->val)
                        ans = l1, l1 = l1->next;
                    else
                        ans = l2, l2 = l2->next;
                }
                
                else if(l1)
                    ans = l1, l1 = l1->next;
                else
                    ans = l2, l2 = l2->next;
                
                prev = ans;
                continue;
            }
            
            if(l1 && l2){
                if(l1->val < l2->val)
                    curr = l1, l1 = l1->next;
                else
                    curr = l2, l2 = l2->next;
            }
                
            else if(l1)
                curr = l1, l1 = l1->next;
            else
                curr = l2, l2 = l2->next;
            
            prev->next = curr;
            prev = curr;
        }
        
        return ans;
    }
};
