/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    map<int, vector<Node*>> mp;
    
    void dfs(Node* root, int level)
    {
        if(root == NULL) return;
        
        mp[level].push_back(root);
        
        dfs(root->left, level + 1);
        dfs(root->right, level + 1);
    }
    
    Node* connect(Node* root) {
        dfs(root, 0);
        
        auto itr = mp.begin();
        while(itr != mp.end())
        {
            for(int i = 0; i < itr->second.size() - 1; i++)
            {
                itr->second[i]->next = itr->second[i + 1];
            }
            
            itr++;
        }
        
        return root;
    }
};
