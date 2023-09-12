// Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
// Accepted 2023-09-12 04:58 UTC · C++ · 21 ms · 15.8 MB

class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int elem_sum = 0, digit_sum = 0;
        for (auto& num : nums) {
            elem_sum += num;
            auto digit_str = to_string(num);
            for (auto& ch : digit_str) {
                digit_sum += ch - '0';
            }
        }
        return elem_sum - digit_sum;
    }
};
