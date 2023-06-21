// Throttle
// https://leetcode.com/problems/throttle/
// Accepted 2023-06-21 20:28 UTC · JavaScript · 71 ms · 41.5 MB

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let timeout
    let nextCallTime = 0
    return (...args) => {
        const delay = Math.max(0, nextCallTime - Date.now())
        clearTimeout(timeout)
        timeout = setTimeout(() => {
            fn(...args)
            nextCallTime = Date.now() + t
        }, delay)
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
