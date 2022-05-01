public class Solution {
    public IList<string> FizzBuzz(int n) {
        List<string> ans = new List<string>();
        
        string temp = "";
        for(int i = 1; i <= n; i++) {
            temp = "";
            
            if(i % 3 == 0)
                temp += "Fizz";
            if(i % 5 == 0)
                temp += "Buzz";
            
            if(i % 3 != 0 && i % 5 != 0)
                temp = i.ToString();
            
            ans.Add(temp);
        }
        
        return ans;
    }
}
