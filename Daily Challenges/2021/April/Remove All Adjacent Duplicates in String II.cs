public class Solution
{
    public string RemoveDuplicates(string s, int k)
    {
        int length = s.Length;
        Stack<Tuple<char, int>> stk = new Stack<Tuple<char, int>>();


        for(int i = 0; i < length; i++)
        {
            if (stk.Count == 0) stk.Push(new Tuple<char, int>(s[i], 1));
            else
            {
                if(stk.Peek().Item1 == s[i])
                {
                    if(stk.Peek().Item2 == k - 1)
                    {
                        for (int j = 1; j <= k - 1; j++) stk.Pop();
                    }

                    else stk.Push(new Tuple<char, int>(s[i], 1 + stk.Peek().Item2));
                }

                else stk.Push(new Tuple<char, int>(s[i], 1));
            }
        }

        string temp = "";
        while(stk.Count > 0)
        {
            temp += stk.Peek().Item1;
            stk.Pop();
        }

        string ans = "";
        for (int i = temp.Length - 1; i >= 0; i--) ans += temp[i];

        return ans;
    }
}
