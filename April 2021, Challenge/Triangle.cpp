class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if(triangle.size() == 1) return triangle[0][0];
        
        vector<int> up, down;
        
        up.push_back(triangle[0][0]);
        for(int i = 1; i < triangle.size(); i++)
        {
            down.clear();
            down.push_back(up[0] + triangle[i][0]);
            
            for(int j = 1; j < triangle[i].size() - 1; j++)
                down.push_back(triangle[i][j] + min(up[j], up[j - 1]));
            
            down.push_back(triangle[i].back() + up.back());
            
            up.clear();
            for(int e : down) up.push_back(e);
        }
        
        int ans = 999999999;
        for(int e : down) ans = min(ans, e);
        
        return ans;
    }
};
