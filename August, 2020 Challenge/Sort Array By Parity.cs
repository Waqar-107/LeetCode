public class Solution {
    public int[] SortArrayByParity(int[] A) {
        int[] ans = new int[A.Length];
        
        int idx = 0;
        for(int i = 0; i < A.Length; i++) {
            if(A[i] % 2 == 0) ans[idx++] = A[i];
        }
        
        for(int i = 0; i < A.Length; i++) {
            if(A[i] % 2 == 1) ans[idx++] = A[i];
        }
        
        return ans;
    }
}
