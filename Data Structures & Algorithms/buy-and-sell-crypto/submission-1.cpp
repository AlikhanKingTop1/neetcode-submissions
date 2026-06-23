class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for (int i = 0; i < prices.size(); i++) {
            int buy = prices[i];
            for (int j = i + 1; j < prices.size(); j++) {
                int sell = prices[j];
                profit = myMax(profit, sell - buy);
            }
        }
        return profit;
    }
    int myMax(int a, int b) {
    if (a < b)
        return b;
    else
        return a;
    }
};