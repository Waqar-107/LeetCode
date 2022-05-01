public class Solution {
    public bool IsPalindrome(string s) {
        s = s.ToLower();
        string t = "";

        for(int k = 0; k < s.Length; k++)
        {
            if (s[k] >= 'a' && s[k] <= 'z') t += s[k];
            else if(s[k] >= '0' && s[k] <= '9') t += s[k];
        }

        int i = 0;
        int j = t.Length - 1;

        while(i < j)
        {
            if (t[i] != t[j]) return false;
            i++;
            j--;
        }

        return true;
    }
}
