class Solution {
public:
    bool isRobotBounded(string instructions) {
        char ch[4] = {'N', 'E', 'S', 'W'};
        int curr = 0;
        pair<int, int> pos = {0, 0};
        
        for(int i = 0; i < instructions.length(); i++){
            if(instructions[i] == 'L') curr = (curr - 1 + 4) % 4;
            else if(instructions[i] == 'R') curr = (curr + 1) % 4;
            
            else {
                if(ch[curr] == 'N') pos.second++;
                else if(ch[curr] == 'S') pos.second--;
                else if(ch[curr] == 'E') pos.first++;
                else pos.first--;
            }
        }
        
        return (pos.first == 0 &&   pos.second == 0) || (ch[curr] != 'N');
    }
};
