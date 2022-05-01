public class Solution {
    public int LongestPalindrome(string s) {
        IDictionary<char, int> dict = new Dictionary<char, int>();

        for(int i = 0; i < s.Length; i++)
        {
            if (dict.ContainsKey(s[i])) dict[s[i]] += 1;
            else dict[s[i]] = 1;
        }

        bool flag = false;
        int cnt = 0;

        foreach(char key in dict.Keys)
        {
            if (dict[key] % 2 == 1) {
                cnt += (dict[key] - 1);
                flag = true;
            }
            
            else cnt += dict[key];
        }
        
        
        if(flag) cnt++;
        
        return cnt;
    }
}
