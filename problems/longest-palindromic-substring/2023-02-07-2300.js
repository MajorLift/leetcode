// Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/
// Accepted 2023-02-07 23:00 UTC · JavaScript · 90 ms · 43 MB

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    function expand(l, r) {
        while (l >= 0 && r < s.length && s[l] === s[r] && l-- <= r++);
        return --r - ++l + 1
    }
    let [global_max, start, end] = [0, 0, 0]
    for (let i = 0; i < s.length; ++i) {
        const local_max = Math.max(expand(i, i + 1), expand(i - 1, i + 1))
        if (local_max > global_max) {
            [global_max, start, end] = [local_max, i - Math.floor((local_max - 1) / 2), i + Math.floor(local_max / 2)]
        }
    }
    return s.slice(start, ++end)
}
