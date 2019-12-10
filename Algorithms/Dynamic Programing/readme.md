[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) : **The problem is known as kadanes algorithm. We use two variables to keep track of the maximum sum. We keep a sum variable. For each integer we add it to the sum variable. if it is positive then no problem but if it is negative then make it 0. In each iteration compare the maximum with the current sum.**

**The maximum sum of sub-array will be a contiguous sub-array of positive numbers, so when ever the sum becomes less than 0 we reset it to 0. If all n numbers are negative then the ans will be the minimum of the array**

[392. Is Subsequence](https://leetcode.com/problems/is-subsequence/) : **Solved it without dp. A variable is pointing the first char of the string s. In a loop we iterate the string t. If current char is equal to the char that variable is pointing then we move the variable farther. If the variable reaches the end of the string s then it means s can be acquired from t**

[746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) : **we can start at either at 0 or 1, so cost to reach these two is 0. now for the stairs >= 2, we can reach here either from i-1 th stair or i-2 th stair**

[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) : **return (n+1)th fibonacci**

[198. House Robber](https://leetcode.com/problems/house-robber/) : **if we are going to take ith then we can't take (i-1) so max we get is cost[i] + cost of i - 2. if we take (i-1) then we won't take ith** 

[303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) : **straight forward problem, pre-calculate sum, store sum of 1 to i where 1 <= i <= n**

[338. Counting Bits](https://leetcode.com/problems/counting-bits/) : **the problem is solved in a recursive approach. we generate all the numbers from 1 to n. we start with 0, from 0 we make 01 and 00, from 01 we make...**
