// Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/
// Accepted 2023-06-19 23:11 UTC · JavaScript · 58 ms · 42.3 MB

Array.prototype.last = function() {
    return this.length ? this[this.length - 1] : -1
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
