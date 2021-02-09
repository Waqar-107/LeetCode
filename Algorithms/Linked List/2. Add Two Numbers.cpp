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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *ans, *prev = NULL;
        
        int carry = 0;
        while(l1 || l2)
        {
            ListNode *temp = new ListNode(-1);
            if(prev == NULL)
                ans = temp;
            else
                prev->next = temp;
            
            if(l1 && l2)
            {
                carry += (l1->val + l2->val);
                temp->val = (carry % 10);
                carry /= 10;
                
                l1 = l1->next;
                l2 = l2->next;
            }
            
            else if(l1)
            {
                carry += l1->val;
                temp->val = (carry % 10);
                carry /= 10;
                
                l1 = l1->next;
            }
            
            else
            {
                carry += l2->val;
                temp->val = (carry % 10);
                carry /= 10;
                
                l2 = l2->next;
            }
            
            prev = temp;
        }
        
        if(carry)
        {
            ListNode *temp = new ListNode(carry);
            prev->next = temp;
        }
        
        return ans;
    }
};
