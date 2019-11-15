/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    int solve(Node *root, int d)
    {
        int mx = d;
        if(root == NULL) return mx;
        
        for(Node* e : root->children)
            mx = max(mx, solve(e, d + 1));
        
        return mx;
    }
    
    int maxDepth(Node* root) {
        if(root == NULL) return 0;
        
        return solve(root, 1);
    }
};
