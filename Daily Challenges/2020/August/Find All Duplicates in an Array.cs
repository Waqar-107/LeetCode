public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        IDictionary<int, int> cnt = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++)
        {
            if (cnt.ContainsKey(nums[i])) cnt[nums[i]]++;
            else cnt.Add(nums[i], 1);
        }

        IList<int> ans = new List<int>();

        foreach(int k in cnt.Keys)
        {
            if (cnt[k] == 2) ans.Add(k);
        }

        return ans;
    }
}
