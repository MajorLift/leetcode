// Regular Expression Matching
// https://leetcode.com/problems/regular-expression-matching/
// Accepted 2023-03-13 22:48 UTC · JavaScript · 76 ms · 45.3 MB

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const memo = Array.from({ length: s.length + 1 }, () => new Array(p.length + 1).fill(false))
    memo[s.length][p.length] = true
    for (let i = s.length; i >= 0; --i) {
        for (let j = p.length - 1; j >= 0; --j) {
            let is_curr_match = i < s.length && (p[j] === s[i] || p[j] === ".")
            if (j < p.length - 1 && p[j + 1] == "*") {
                memo[i][j] = memo[i][j + 2] || (is_curr_match && memo[i + 1][j])
            } else memo[i][j] = is_curr_match && memo[i + 1][j + 1]
        }
    }
    return memo[0][0]
};
