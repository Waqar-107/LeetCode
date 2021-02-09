/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int p = 1;
    public int ans = 0;
    
    public void solve(ListNode head) {
        if(head == null) return;
        
        solve(head.next);
        this.ans += head.val * this.p;
        this.p *= 2;
    }
    
    public int getDecimalValue(ListNode head) {
        int ans = 0;
        while(head != null) {
            ans = (ans << 1) + head.val;
            head = head.next;
        }
        
        return ans;
    }
}