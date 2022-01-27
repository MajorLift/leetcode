// Range Addition
// https://leetcode.com/problems/range-addition/
// Accepted 2022-01-27 17:34 UTC · JavaScript · 708 ms · 50.9 MB

/**
 * @param {number} length
 * @param {number[][]} updates
 * @return {number[]}
 */
var getModifiedArray = function(length, updates) {
    const output = new Array(length).fill(0);
    for (const [start, end, inc] of updates)
        for (let i = start; i <= end; i += 1) output[i] += inc;
    return output;
};
