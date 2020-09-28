/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    map<int, Node*> vis;
    Node* dfs(Node* root){
        if(root == NULL) return NULL;
        
        Node* newRoot = new Node(root->val);
        
        vis[root->val] = newRoot;
        for(int i = 0; i < root->neighbors.size(); i++){
            if(vis[root->neighbors[i]->val]) {
                newRoot->neighbors.push_back(vis[root->neighbors[i]->val]);
                continue;
            }
            
            Node* to = dfs(root->neighbors[i]);
            newRoot->neighbors.push_back(to);
        }
        
        return newRoot;
    }
    Node* cloneGraph(Node* node) {
        return dfs(node);
    }
};
