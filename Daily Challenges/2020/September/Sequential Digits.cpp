class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> ans;
        
        for(int i = 1; i <= 9; i++){
            for(int j = 1; j <= 9 - i + 1; j++){
                // starts with j, length of the number is i
                int num = 0;
                for(int k = 1; k <= i; k++)
                    num = num * 10 + (j + k - 1);
                
                if(low <= num && num <= high) ans.push_back(num);
            }
        }
        
        return ans;
    }
};
