// Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/
// Accepted 2022-02-02 16:58 UTC · JavaScript · 160 ms · 46.5 MB

/**
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function(s) {
    const map = s.split('').reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1;
        return acc;
    }, {});
    for (let i = 0; i < s.length; i++) {
        if (!map[s[i].toLowerCase()] || !map[s[i].toUpperCase()]) {
            const [s1, s2] = [longestNiceSubstring(s.slice(0, i)), longestNiceSubstring(s.slice(i + 1))];
            return s1.length >= s2.length ? s1 : s2;
        }
    }
    return s;
};
