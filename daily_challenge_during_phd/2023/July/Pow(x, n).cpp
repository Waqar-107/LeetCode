class Solution {
public:
    double solve(double x, long long int n) {
        if(n == 0) return 1.0;
        if(n == 1) return x;

        if(n % 2 == 0) {
            double temp = solve(x, n / 2);
            return temp * temp;
        }

        return x * solve(x, n - 1);
    }
    double myPow(double x, int n) {
        if(n < 0) {
            long long int newN = n;
            newN *= -1;

            return 1.0 / solve(x, newN); 
        }

        return solve(x, (long long int) n);
    }
};
