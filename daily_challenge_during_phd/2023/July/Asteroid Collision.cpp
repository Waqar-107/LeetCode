class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> stk;

        for(int i = 0; i < asteroids.size(); i++) {
            if(asteroids[i] < 0) {
                if(stk.empty()) {
                    stk.push(asteroids[i]);
                    continue;
                }

                while(!stk.empty()) {
                    if(stk.top() < 0) {
                        stk.push(asteroids[i]);
                        break;
                    } else {
                        if(stk.top() == asteroids[i] * -1) {
                            stk.pop();
                            break;
                        } else if(stk.top() < asteroids[i] * -1) {
                            stk.pop();
                            if(stk.empty()) {
                                stk.push(asteroids[i]);
                                break;
                            }
                        } else break;
                    }
                }
            } else {
                stk.push(asteroids[i]);
            }
        }

        vector<int> ans;
        while(!stk.empty()) {
            ans.push_back(stk.top());
            stk.pop();
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
