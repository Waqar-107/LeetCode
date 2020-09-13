bool cmp(vector<int> a, vector<int> b){
    if(a[0] == b[0]) return a[1] < b[1];
    return a[0] < b[0];
}

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int flag = -2;
        for(int i = 0; i < intervals.size(); i++)
        {
            // new interval completely belongs to an existing one
            if(intervals[i][0] <= newInterval[0] && newInterval[1] <= intervals[i][1])
                return intervals;
            
            // new intervals starting falls in the range of existing
            else if(intervals[i][0] <= newInterval[0] && newInterval[0] <= intervals[i][1] && newInterval[1] >= intervals[i][1]){
                flag = i; 
                break;
            }
            
            // new intervals ending falls in the range of existing
            else if(newInterval[0] <= intervals[i][0] && newInterval[1] >= intervals[i][0] && newInterval[1] <= intervals[i][1]){
                flag = i;
                break;
            }
            
            // interval belongs to the new one
            else if(newInterval[0] <= intervals[i][0] && intervals[i][1] <= newInterval[1]){
                flag = i;
                break;
            }
        }
        
        if(flag == -2)
        {
            intervals.push_back(newInterval);
            sort(intervals.begin(), intervals.end(), cmp);
            return intervals;
        }
        
      
        // start merging with the flag idx and continue till you manage to find non-clash
        vector<vector<int>> ans;
        for(int i =0; i < flag; i++) ans.push_back(intervals[i]);
        
        newInterval[0] = min(intervals[flag][0], newInterval[0]);
        newInterval[1] = max(intervals[flag][1], newInterval[1]);
        flag++;
        
        while(flag < intervals.size())
        {
            if(intervals[flag][0] >newInterval[1])
            {
                // no clash found
                ans.push_back(newInterval);
                while(flag < intervals.size()){
                    ans.push_back(intervals[flag]);
                    flag++;
                }
                
                flag = -1;
                break;
            }
            
            else
            {
                newInterval[0] = min(intervals[flag][0], newInterval[0]);
                newInterval[1] = max(intervals[flag][1], newInterval[1]);
                flag++;
            }
        }
        
        if(flag != -1) ans.push_back(newInterval);
        return ans;
    }
};
