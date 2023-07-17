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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1, s2;
        while(l1) {
            s1.push(l1->val);
            l1 = l1->next;
        }

        while(l2) {
            s2.push(l2->val);
            l2 = l2->next;
        }

        vector<int> vec;
        int sum, rem = 0;

        while(s1.size() && s2.size()) {
            sum = s1.top() + s2.top() + rem;
            rem = sum / 10;
            sum = sum % 10;

            vec.push_back(sum);
            s1.pop(); s2.pop();
        }

        while(s1.size()) {
            sum = s1.top() + rem;
            rem = sum / 10;
            sum = sum % 10;

            vec.push_back(sum);
            s1.pop();
        }

        while(s2.size()) {
            sum = s2.top() + rem;
            rem = sum / 10;
            sum = sum % 10;

            vec.push_back(sum);
            s2.pop();
        }

        if(rem) {
            vec.push_back(rem);
        }

        for(int e : vec)
            cout << e << " ";

        ListNode *ans, *prev, *newNode;
        ans = new ListNode(vec[vec.size() - 1]);

        prev = ans;
        
        for(int i = vec.size() - 2; i >= 0; i--) {
            newNode = new ListNode(vec[i]);
            prev->next = newNode;
            prev = newNode;
        }

        return ans;
    }
};
