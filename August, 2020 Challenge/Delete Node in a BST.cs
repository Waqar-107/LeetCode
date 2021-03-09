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
public class pair
{
    public TreeNode f, s;
    public pair() { }
    public pair(TreeNode f, TreeNode s)
    {
        this.f = f;
        this.s = s;
    }
}

public class Solution
{
    public pair find(TreeNode root, TreeNode parent, int val)
    {
        if (root == null) return new pair();

        if (root.val == val) return new pair(root, parent);

        if (root.val > val) return find(root.left, root, val);
        return find(root.right, root, val);
    }

    public pair findMin(TreeNode root, TreeNode parent)
    {
        if (root != null && root.left != null) return findMin(root.left, root);
        return new pair(root, parent);
    }

    public void delete(TreeNode root, TreeNode parent)
    {
        // leaf node
        if(root.left == null && root.right == null)
        {
            // update the parent node
            if (parent != null && parent.right == root)
                parent.right = null;
            if (parent != null && parent.left == root)
                parent.left = null;
        }

        // has one child
        else if(root.left != null && root.right == null)
        {
            if (parent != null && parent.right == root)
                parent.right = root.left;
            if (parent != null && parent.left == root)
                parent.left = root.left;
        }

        // has one child
        else if (root.left == null && root.right != null)
        {
            if (parent != null && parent.right == root)
                parent.right = root.right;
            if (parent != null && parent.left == root)
                parent.left = root.right;
        }

        else
        {
            pair res = findMin(root.right, root);
            root.val = res.f.val;

            delete(res.f, res.s);
        }
    }

    public TreeNode DeleteNode(TreeNode root, int key)
    {
        if (root == null) return null;

        pair res;
        if(root.val == key)
        {
            if (root.left == null && root.right == null)
                return null;

            else if (root.left != null && root.right == null)
                return root.left;

            else if (root.right != null && root.left == null)
                return root.right;

            else
            {
                res = findMin(root.right, root);
                root.val = res.f.val;
                delete(res.f, res.s);

                return root;
            }
        }

        res = find(root, null, key);

        if (res.f == null) return root;

        delete(res.f, res.s);
        return root;
    }
}
