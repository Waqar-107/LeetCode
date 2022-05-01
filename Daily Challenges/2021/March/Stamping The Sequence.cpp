class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        int n = target.length();
        int m = stamp.length();
        
        vector<int> ans;
        
        bool flag;
        int cnt, mx, idx;
        while(true)
        {
            mx = 0;
            idx = -1;
            
            for(int i = 0; i < n - m + 1; i++) {
                flag = true;
                cnt = 0;
                
                for(int j = 0; j < m; j++) {
                    if(target[i + j] == '?') continue;
                    else if(target[i + j] == stamp[j]) cnt++;
                    else {
                        flag = false;
                        break;
                    }
                }
                
                if(flag) {
                    if(cnt && mx < cnt)
                        mx = cnt, idx = i;
                }
            }
            
            if(idx == -1) break;
            
            for(int j = idx; j < idx + m; j++)
                target[j] = '?';
            ans.push_back(idx);
        }
        
        flag = false;
        for(int i = 0; i < n; i++) {
            if(target[i] != '?') {
                flag = true;
                break;
            }
        }
        
        if(flag) ans.clear();
        
        reverse(ans.begin(), ans.end());
        return ans;
    }
};class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        int n = target.length();
        int m = stamp.length();
        
        vector<int> ans;
        
        bool flag;
        int cnt, mx, idx;
        while(true)
        {
            mx = 0;
            idx = -1;
            
            for(int i = 0; i < n - m + 1; i++) {
                flag = true;
                cnt = 0;
                
                for(int j = 0; j < m; j++) {
                    if(target[i + j] == '?') continue;
                    else if(target[i + j] == stamp[j]) cnt++;
                    else {
                        flag = false;
                        break;
                    }
                }
                
                if(flag) {
                    if(cnt && mx < cnt)
                        mx = cnt, idx = i;
                }
            }
            
            if(idx == -1) break;
            
            for(int j = idx; j < idx + m; j++)
                target[j] = '?';
            ans.push_back(idx);
        }
        
        flag = false;
        for(int i = 0; i < n; i++) {
            if(target[i] != '?') {
                flag = true;
                break;
            }
        }
        
        if(flag) ans.clear();
        
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
