// Word Break
// https://leetcode.com/problems/word-break/
// Accepted 2023-02-16 01:27 UTC · JavaScript · 81 ms · 44.5 MB

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const memo = new Array(s.length).fill(null)
    return (function dp(start = 0) {
        if (start === s.length) return true
        if (memo[start] !== null) return memo[start]
        for (let end = start + 1; end < s.length + 1; ++end) {
            if (wordSet.has(s.slice(start, end)) && dp(end)) {
                return memo[end] = true
            }
        }
        return memo[start] = false
    })()
};
