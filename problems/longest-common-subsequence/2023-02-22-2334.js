// Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/
// Accepted 2023-02-22 23:34 UTC · JavaScript · 132 ms · 68.2 MB

/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const memo = Array.from({ length: text1.length }, () => new Array(text2.length).fill(0))
    for (let i = 0; i < text1.length; ++i) {
        for (let j = 0; j < text2.length; ++j) {
            memo[i][j] = text1[i] === text2[j] 
                ? 1 + ((memo[i - 1] ?? [])[j - 1] ?? 0)
                : Math.max(((memo[i - 1] ?? [])[j] ?? 0), ((memo[i] ?? [])[j - 1] ?? 0))
        }
    }
    return memo[text1.length - 1][text2.length - 1]
}
