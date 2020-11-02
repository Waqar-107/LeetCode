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
    void deleteNode(ListNode* node) {
        // the node to be deleted is given
        // for each node assign the next nodes val, delete the tail
        
        ListNode *parent = NULL;
        while(node){
            if(node->next)
            {
                node->val = node->next->val;
                parent = node;
                node = node->next;
            }
            
            else {
                // delete node
                if(parent) parent->next = NULL;
                delete node;
                break;
            }
        }
    }
};
