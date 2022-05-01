public class Solution {
    public int TitleToNumber(string columnTitle) {
        int p = 1;
        int ans = 0;
        
        for(int i = columnTitle.Length - 1; i >= 0; i--) {
            ans += (p * (int)(columnTitle[i] - 'A' + 1));
            p *= 26;
        }
        
        return ans;
    }
}
