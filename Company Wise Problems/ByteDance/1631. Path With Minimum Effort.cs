public class Solution
{
    int r, c;
    int[] dx, dy;
    IDictionary<Tuple<int, int>, bool> vis;
    
    public Solution()
    {
        vis = new Dictionary<Tuple<int, int>, bool>();
        dx = new int[4] { 1, -1, 0, 0 };
        dy = new int[4] { 0, 0, 1, -1 };
    }

    public bool IsInside(Tuple<int, int> src)
    {
        return (src.Item1 >= 0 && src.Item2 >= 0 && src.Item1 < r && src.Item2 < c);
    }

    public void DFS(int[][] heights, int threshold, Tuple<int, int> src)
    {
        vis.Add(src, true);

        for (int i = 0; i < 4; i++)
        {
            Tuple<int, int> nxt = new Tuple<int, int>(dx[i] + src.Item1, dy[i] + src.Item2);

            if (IsInside(nxt) && !vis.ContainsKey(nxt) && Math.Abs(heights[nxt.Item1][nxt.Item2] - heights[src.Item1][src.Item2]) <= threshold)
                DFS(heights, threshold, nxt);
        }
    }

    public int MinimumEffortPath(int[][] heights)
    {
        int hi = 0, lo = 0;

        r = heights.Length;
        c = heights[0].Length;

        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
                hi = Math.Max(hi, heights[i][j]);      
        }

        Tuple<int, int> src = new Tuple<int, int>(0, 0);
        Tuple<int, int> dest = new Tuple<int, int>(r - 1, c - 1);
        int ans = hi;

        while (lo <= hi)
        {
            int mid = (hi + lo) / 2;
            DFS(heights, mid, src);
            
            if (vis.ContainsKey(dest))
            {
                ans = Math.Min(ans, mid);
                hi = mid - 1;
            }

            else
                lo = mid + 1;
            
            vis.Clear();
        }

        return ans;
    }
}
