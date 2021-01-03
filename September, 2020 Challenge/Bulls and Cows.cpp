class Solution {
public:
    string toStr(int n)
    {
        if(!n) return "0";
        
        string s;
        while(n)
        {
            s.push_back(char(n % 10 + '0'));
            n /= 10;
        }
        
        reverse(s.begin(), s.end());
        return s;
    }
    
    string getHint(string secret, string guess) {
        int n = secret.length();
        int cows = 0, bulls = 0;
        
        for(int i = 0; i < n; i++)
        {
            if(secret[i] == guess[i])
            {
                secret[i] = '#';
                guess[i] = '#';
                bulls++;
            }
        }
        
        map<char, int> mp;
        for(int i = 0; i < n; i++)
        {
            if(secret[i] != '#')
                mp[secret[i]]++;
        }
        
        
        for(int i = 0; i < n; i++)
        {
            if(guess[i] != '#')
            {
                if(mp[guess[i]])
                {
                    cows++;
                    mp[guess[i]]--;
                }
            }
        }
        
        return toStr(bulls) + "A" + toStr(cows) + "B";
    }
};
