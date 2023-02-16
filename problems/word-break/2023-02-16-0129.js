// Word Break
// https://leetcode.com/problems/word-break/
// Accepted 2023-02-16 01:29 UTC · JavaScript · 85 ms · 44.1 MB

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const memo = [true, ...new Array(s.length).fill(false)]
    for (let r = 1; r <= s.length; ++r) {
        for (let l = 0; l < r; ++l) {
            if (wordSet.has(s.slice(l, r)) && memo[l]) {
                memo[r] = true
                break
            }
        }
    }
    return memo[s.length]
};
