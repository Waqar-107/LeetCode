public class Solution {
    public IList<int> GetRow(int rowIndex)
    {
        List<int> ret = new List<int>();

        for (int i = 0; i <= Math.Min(1, rowIndex); i++) 
            ret.Add(1);

        if (rowIndex <= 1) return ret;

        for(int i = 2; i <= rowIndex; i++)
        {
            List<int> newLst = new List<int>();
            newLst.Add(ret[0]);

            for (int j = 0; j < ret.Count - 1; j++)
                newLst.Add(ret[j] + ret[j + 1]);

            newLst.Add(ret[ret.Count - 1]);

            ret.Clear();
            foreach (int e in newLst) ret.Add(e);
        }

        return ret;
    }
}
