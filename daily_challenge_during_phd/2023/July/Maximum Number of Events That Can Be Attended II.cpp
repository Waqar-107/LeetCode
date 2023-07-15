bool cmp(vector<int> one, vector<int> two) {
    return one[0] < two[0];
}

class Solution {
public:
    int binary_search(vector<vector<int>>& events, int target) {
        int lo = 0, hi = events.size(), mid;

        while(lo < hi) {
            mid = (lo + hi) / 2;

            if(events[mid][0] == target) return mid;
            else if(events[mid][0] > target) hi = mid;
            else lo = mid + 1;
        }

        return lo;
    }

    int dfs(vector<vector<int>>& events, int currentEvent, int k, vector<vector<int>>& dp) {
        if(k <= 0 || currentEvent > events.size()) return 0;
        if(dp[k][currentEvent]) return dp[k][currentEvent];

        // take the event
        int nextEvent = binary_search(events, events[currentEvent - 1][1] + 1) + 1;
        
        int take = events[currentEvent - 1][2] + dfs(events, nextEvent, k - 1, dp);

        // skip the event
        int skip = dfs(events, currentEvent + 1, k, dp);

        return dp[k][currentEvent] = max(take, skip);
    }

    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 0));

        sort(events.begin(), events.end(), cmp);

        return dfs(events, 1, k, dp);
    }
};
