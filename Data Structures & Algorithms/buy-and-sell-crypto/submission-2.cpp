class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;  // минимальная цена
        int maxProfit = 0;       // максимальная прибыль

        for (int i = 0; i < prices.size(); i++) {
            minPrice = min(minPrice, prices[i]);  // обновляем минимальную цену
            maxProfit = max(maxProfit, prices[i] - minPrice);  // обновляем максимальный профит
        }
        return maxProfit;
    }
};