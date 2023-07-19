bool cmp(vector<int> &a, vector<int> &b) {
    return a[1] < b[1];
}

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size() == 0) return 0;

        sort(intervals.begin(), intervals.end(), cmp);

        int taken = 0, last_intervals_end_time = -60000;
        for(int i = 0; i < intervals.size(); i++) {
            // cout << "i " << i << " " << last_intervals_end_time << endl;
            if(intervals[i][0] >= last_intervals_end_time)
                taken++, last_intervals_end_time = intervals[i][1]; 
        }

        return intervals.size() - taken;
    }
};
