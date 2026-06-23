class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for (int i = 0; i <=  nums.size(); i += 1) {
            for(int j = i + 1; j < nums.size(); j += 1) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};