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
    queue<int> q;
    stack<ListNode*> stk;
    void solve(ListNode* head, int num, int k)
    {
        q.push(head->val);
        stk.push(head);
        
        if(num % k == 0)
        {
            while(stk.size())
            {
                stk.top()->val = q.front();
                stk.pop(), q.pop();
            }
        }
        
        if(head->next)
            solve(head->next, num + 1, k);
        
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head)
            solve(head, 1, k);
        return head;
    }
};
