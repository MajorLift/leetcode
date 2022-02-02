// Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
// Accepted 2022-02-02 20:06 UTC · JavaScript · 109 ms · 46.5 MB

/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function(s) {
    let output = 0;
    const arr = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        arr[s[i].charCodeAt(0) - "a".charCodeAt(0)]++;
    }
    arr.sort((a, b) => b - a);
    for (let i = 1; i < 26; i++) {
        while (arr[i] && arr[i] >= arr[i - 1]) {
            arr[i]--;
            output++;
        }
    }
    return output;
};
