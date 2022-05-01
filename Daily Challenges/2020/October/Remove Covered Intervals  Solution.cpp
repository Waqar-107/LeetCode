class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if(n == 0) return 0;
        
        vector<pair<int, int>> vec;
        for(int i = 0; i < intervals.size(); i++)
            vec.push_back({intervals[i][0], intervals[i][1]});
        
        sort(vec.begin(), vec.end());
        
        stack<pair<int, int>> stk;
        stk.push(vec[0]);
        
        for(int i = 1; i < vec.size(); i++)
        {
            pair<int, int> u = stk.top();
            
            if(vec[i].first == u.first){
                u.second = max(u.second, vec[i].second);
                stk.pop();
                stk.push(u);
            }
            
            else {
                if(vec[i].first >= u.first && vec[i].first <= u.second && vec[i].second >= u.first && vec[i].second <= u.second) continue;
                else stk.push(vec[i]);
            }
        }
        
        
        return stk.size();
    }
};
