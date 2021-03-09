/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public void ReorderList(ListNode head) {
        LinkedList<ListNode> lst = new LinkedList<ListNode>();
        ListNode temp = head;
        
        while(temp != null)
        {
            lst.AddLast(temp);
            temp = temp.next;
        }

        while(lst.Count > 2)
        {
            ListNode x = lst.First.Value;
            ListNode y = lst.Last.Value;
            
            Console.WriteLine(x.val + " " + y.val);

            y.next = x.next;
            x.next = y;

            lst.RemoveFirst();
            lst.RemoveLast();

            if(lst.Count > 0)
                lst.Last.Value.next = null;
        }
    }
}
