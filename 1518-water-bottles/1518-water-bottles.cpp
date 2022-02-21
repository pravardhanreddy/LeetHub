class Solution {
public:
    int solve(int numBottles, int numExchange, int rem) {
        if(numBottles == 0 and rem < numExchange) return 0;
        
        return numBottles + solve((numBottles+rem)/numExchange, numExchange, (numBottles+rem)%numExchange);
    }
    int numWaterBottles(int numBottles, int numExchange) {
        return solve(numBottles, numExchange, 0);
    }
};