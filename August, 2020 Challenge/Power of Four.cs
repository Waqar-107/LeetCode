public class Solution {
    public bool IsPowerOfFour(int n) {
        if(n == 0) return false;
            
        double q = Math.Log(n) / Math.Log(4);
        if (q == Math.Floor(q)) return true;
        return false;
    }
}
