/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void DeleteNode(ListNode node) {
        ListNode parent = node;
        while(node != null) {
            if(node.next == null) {
                parent.next = null;
                break;
            }
            
            else {
                node.val = node.next.val;
                parent = node;
                node = node.next;
            }
        }
    }
}
