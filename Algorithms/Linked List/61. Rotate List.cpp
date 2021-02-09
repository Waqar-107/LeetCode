/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL || k == 0) return head;
        
        int cnt = 0;
        ListNode* newHead = head;
        
        while(newHead){
            cnt++;
            newHead = newHead->next;
        }
        
        int r = k % cnt;
        if(r == 0) return head;
        
        int curr = 0;
        newHead = head;
        ListNode* parent = NULL;
        
        while(newHead){
            curr++;
            if(curr == cnt - r + 1)
            {
                if(parent) parent->next = NULL;
                break;
            }
            
            parent = newHead;
            newHead = newHead->next;
        }
        
        ListNode* temp = newHead;
        while(true){
            if(temp->next == NULL){
                temp->next = head;
                break;
            }
            
            temp = temp->next;
        }
        
        return newHead;
    }
};