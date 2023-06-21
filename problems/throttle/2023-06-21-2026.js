// Throttle
// https://leetcode.com/problems/throttle/
// Accepted 2023-06-21 20:26 UTC · JavaScript · 63 ms · 42.1 MB

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let interval = null
    let argsQueued = null

    return function(...args) {
        if (interval !== null) {
            argsQueued = args
            return
        }

        fn(...args)
        interval = setInterval(() => {
            if (argsQueued === null) {
                clearInterval(interval)
                interval = null
            } else {
                fn(...argsQueued)
                argsQueued = null
            }
        }, t)
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
