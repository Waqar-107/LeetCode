public class Solution {
    public int RemovePalindromeSub(string s) {
        if(s.Length == 0) return 0;
        
        int i = 0;
        int j = s.Length - 1;
        bool flag = true;
        
        while(i < j) {
            if(s[i] != s[j]) {
                flag = false;
                break;
            }
            
            i++;
            j--;
        }
        
        if(flag) return 1;
        return 2;
    }
}
