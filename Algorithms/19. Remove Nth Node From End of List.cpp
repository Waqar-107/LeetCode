/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(head == NULL) return head;
        
        int len = 0;
        ListNode *x = head, *prev = NULL;
        
        while(x)
            len++, x = x->next;
        
        int k = 1;
        x = head;
        while(x)
        {
            //cout<<x->val<<" "<<k<<" "<<(len - n +1);nl;
            if(k == len - n + 1)
            {
                //cout<<"inside "<<head->val<<" "<<x->val;nl;
                if(head == x) return head->next;
                prev->next = x->next;
                break;
            }
            
            prev = x;
            x = x->next;
            k++;
        }
        
        return head;
    }
};
