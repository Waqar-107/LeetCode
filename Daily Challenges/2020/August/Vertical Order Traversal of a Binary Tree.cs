/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Node : IComparable<Node>
{
    public int value, r, c;
    public Node() { }
    public Node(int value, int r, int c)
    {
        this.value = value;
        this.r = r;
        this.c = c;
    }

    public int CompareTo(Node other)
    {
        if (this.c != other.c) return this.c.CompareTo(other.c);
        else if(this.r != other.r) return this.r.CompareTo(other.r);
        return this.value.CompareTo(other.value);
    }
}


public class Solution
{
    public List<Node> nodeList;

    public Solution()
    {
        nodeList = new List<Node>();
    }

    public void solve(TreeNode root, int r, int c)
    {
        if (root == null) return;

        nodeList.Add(new Node(root.val, r, c));

        this.solve(root.left, r + 1, c - 1);
        this.solve(root.right, r + 1, c + 1);
    }

    public IList<IList<int>> VerticalTraversal(TreeNode root)
    {
        this.solve(root, 0, 0);
        nodeList.Sort();

        IList<IList<int>> ans = new List<IList<int>>();
        for(int i = 0; i < nodeList.Count; i++)
        {
            if (i == 0 || nodeList[i].c != nodeList[i - 1].c)
                ans.Add(new List<int>());

            ans[ans.Count - 1].Add(nodeList[i].value);
        }

        return ans;
    }
}
