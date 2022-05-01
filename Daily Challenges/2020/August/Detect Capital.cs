public class Solution {
    public bool DetectCapitalUse(string word) {
        int n = word.Length;
        int cnt = 0;
        
        for(int i = 0; i < n; i++) {
            if(word[i] >= 'A' && word[i] <= 'Z') cnt++;
        }
        
        if(cnt == n || cnt == 0) return true;
        else if(cnt == 1 && word[0] >= 'A' && word[0] <= 'Z') return true;
        return false;
    }
}
