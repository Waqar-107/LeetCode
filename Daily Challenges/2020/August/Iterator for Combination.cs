public class CombinationIterator {
    public int nxt = 0;
    public List<string> combinations;

    public CombinationIterator(string characters, int combinationLength)
    {
        combinations = new List<string>();

        int n = characters.Length;
        string temp;

        for(int i = 0; i < (1 << n); i++)
        {
            temp = "";
            for(int j = 0; j < n; j++)
            {
                if ((i & (1 << j)) != 0) 
                    temp += characters[j];
            }
            

            if (temp.Length == combinationLength)
                combinations.Add(temp);
        }
        
        combinations.Sort();
    }

    public string Next()
    {
        string ret = combinations[nxt];
        nxt++;
        return ret;
    }

    public bool HasNext()
    {
        if (nxt >= combinations.Count) return false;
        return true;
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
 */
