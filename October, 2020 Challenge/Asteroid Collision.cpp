class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stk;
        vector<int> ans;
        
        int n = asteroids.size();
        for(int i = 0; i < n; i++)
        {
            if(asteroids[i] > 0) stk.push_back(asteroids[i]);
            else {
                while(stk.size()){
                    if(stk.back() == -asteroids[i]){
                        stk.pop_back();
                        asteroids[i] = 0;
                        break;
                    }
                    
                    else if(stk.back() > -asteroids[i]){
                        asteroids[i] = 0;
                        break;
                    }
                    
                    else stk.pop_back();
                }
                
                if(asteroids[i] != 0)
                    ans.push_back(asteroids[i]);
            }
        }
        
        for(int e : stk) ans.push_back(e);
        return ans;
    }
};
