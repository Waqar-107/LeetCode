class Solution {
public:
    int fib(int N) {
        if(N == 0) return 0;
        else if(N == 1) return 1;
        
        int x = 0, y = 1, curr;
        for(int i = 2; i <= N; i++){
            curr = x + y;
            x = y;
            y = curr;
        }
        
        return curr;
    }
};
