public class Solution {
    public int HIndex(int[] citations) {
        int ans = 0;
        Array.Sort(citations);
        
        int n = citations.Length;
        for(int i = 0; i < n; i++) {
            if(citations[i] >= n - i)
                ans = Math.Max(ans, n - i);
        }
        
        return ans;
    }
}
