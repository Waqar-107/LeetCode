class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> vec;
        int idx[26], n = S.length();
        
        for(int i = 0; i < 26; i++) idx[i] = -1;
        for(int i = 0; i < n; i++) idx[S[i] - 'a'] = max(i, idx[S[i] - 'a']);
        
        int processed_so_far = -1;
        int cnt;
        queue<char> q;
        
        while(processed_so_far + 1 < n)
        {
            processed_so_far++;
            q.push(S[processed_so_far]);
            cnt = 0;
            
            while(!q.empty())
            {
                int u = q.front() - 'a';
                q.pop(); cnt++;
                
                if(idx[u] <= processed_so_far) continue;
                for(int i = processed_so_far + 1; i <= idx[u]; i++) q.push(S[i]);
                processed_so_far = idx[u];
            }
            
            vec.push_back(cnt);
        }
        
        return vec;
    }
};
