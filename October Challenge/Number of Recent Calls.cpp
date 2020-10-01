class RecentCounter {
public:
    vector<int> vec;
    RecentCounter() {
    }
    
    int ping(int t) {
        vec.push_back(t);
        int k = lower_bound(vec.begin(), vec.end(), t - 3000) - vec.begin();
        return vec.size() - k;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
