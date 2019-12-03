/***from dust i have come, dust i will be***/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class cmp{
public:
    bool operator()(ListNode* a, ListNode* b){
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, cmp> pq;
        
        for(ListNode* e : lists)
        {
            if(e)
                pq.push(e);
        }
        
        //while(pq.)
        
        ListNode* ans = NULL;
        ListNode* curr = NULL;
        ListNode* prev = NULL;
        while(!pq.empty())
        {
            curr = pq.top(); pq.pop();
            if(ans == NULL)
                ans = curr;
            else
                prev->next = curr;
            
            prev = curr;
            if(curr)
                curr = curr->next;
            
            if(curr)
                pq.push(curr);
        }
        
        return ans;
    }
};
