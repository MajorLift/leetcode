// Reverse String
// https://leetcode.com/problems/reverse-string/
// Accepted 2022-01-03 21:52 UTC · JavaScript · 141 ms · 46.5 MB

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    for (let i = 0; i < Math.ceil(s.length / 2); i += 1) {
        [s[i], s[s.length - (i + 1)]] = [s[s.length -(i + 1)], s[i]]
    }
};
