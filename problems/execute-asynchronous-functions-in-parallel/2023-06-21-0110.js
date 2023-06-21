// Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/
// Accepted 2023-06-21 01:10 UTC · JavaScript · 88 ms · 42.8 MB

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        let completed = 0
        const output = new Array(functions.length).fill(null)
        for (const [i, func] of functions.entries()) {
            func().then((res) => {
                output[i] = res
                completed += 1
                if (completed === functions.length) resolve(output)
            }).catch((err) => reject(err))
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
