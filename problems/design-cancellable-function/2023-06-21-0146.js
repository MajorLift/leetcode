// Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/
// Accepted 2023-06-21 01:46 UTC · JavaScript · 75 ms · 41.9 MB

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let isCanceled = false
    return [
        () => isCanceled = true,
        (async () => {
            let next = generator.next()
            while (!next.done) {
                try {
                    const nextVal = await next.value
                    next = isCanceled ? generator.throw("Cancelled") : generator.next(nextVal)
                } catch(err) {
                    next = generator.throw(err)
                }
            }
            return next.value
        })()
    ]
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
