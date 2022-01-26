// First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/
// Accepted 2022-01-26 06:28 UTC · JavaScript · 297 ms · 49.6 MB

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const map = s.split('').reduce((acc, curr, i) => {
        if (acc.has(curr)) {
            const [count, idx] = acc.get(curr);
            acc.set(curr, [count + 1, i]);
        }
        else acc.set(curr, [1, i]);
        return acc;
    }, new Map());
    console.log(map)
    for (const [key, value] of map) {
        if (value[0] === 1) return value[1];
    }
    return -1;
};
