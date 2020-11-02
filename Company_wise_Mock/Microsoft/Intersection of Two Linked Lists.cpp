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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int cntA = 0, cntB = 0;
        ListNode *temp;
        
        // cnt nodes in A and B
        temp = headA;
        while(temp) {
            cntA++;
            temp = temp->next;
        }
        
        temp = headB;
        while(temp) {
            cntB++;
            temp = temp->next;
        }
        
        ListNode *A = headA, *B = headB;
        while(cntA >  cntB) {
            cntA--;
            A = A->next;
        }
        
        while(cntB > cntA) {
            cntB--;
            B = B->next;
        }
        
        ListNode *ans = NULL;
        while(A and B){
            if(A == B){
                ans = A;
                break;
            }
            
            A = A->next;
            B = B->next;
        }
        
        return ans;
    }
};
