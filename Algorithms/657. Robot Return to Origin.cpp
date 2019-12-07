/***from dust i have come, dust i will be***/

class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        
        for(char ch : moves)
        {
            if(ch == 'U') x++;
            else if(ch == 'D') x--;
            else if(ch == 'R') y++;
            else y--;
        }
        
        if(x == 0 && y == 0)
            return true;
        
        return false;
    }
};
