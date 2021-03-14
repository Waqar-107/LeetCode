public class Solution {
    public int CoinChange(int[] coins, int amount) {
        int inf = 999999999;

        int[] dp = new int[amount + 1];
        Array.Fill(dp, inf);

        foreach (int c in coins)
        {
            if(c <= amount)
                dp[c] = 1;
        }

        dp[0] = 0;
        for(int i = 1; i <= amount; i++)
        {
            int mn = inf;
            foreach(int c in coins)
            {
                if (i >= c)
                    mn = Math.Min(mn, dp[i - c]);
            }

            if (mn < inf) dp[i] = mn + 1;
        }
        
        if(dp[amount] >= inf) return -1;
        
        return dp[amount];
    }
}
