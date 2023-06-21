// Debounce
// https://leetcode.com/problems/debounce/
// Accepted 2023-06-21 20:02 UTC · JavaScript · 63 ms · 42.3 MB

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeout
    return function(...args) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
            fn(...args)
        }, t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
