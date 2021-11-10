// Jump Game
// https://leetcode.com/problems/jump-game/
// Accepted 2021-11-10 12:50 UTC · JavaScript · 1444 ms · 46 MB

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    const memo = [];
    for (let i = 0; i < nums.length; i += 1) memo.push(false);
    memo[0] = true;
    for (let i = 0; i < nums.length; i += 1) {
        if (memo[i] && nums[i] > 0) {
            for (let j = 1; j <= nums[i]; j += 1) {
                if (i + j < memo.length) memo[i + j] = true;
            }
        }
    }
    return memo[nums.length - 1];
};
