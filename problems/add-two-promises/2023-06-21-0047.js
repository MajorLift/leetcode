// Add Two Promises
// https://leetcode.com/problems/add-two-promises/
// Accepted 2023-06-21 00:47 UTC · JavaScript · 71 ms · 41.7 MB

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return await promise1 + await promise2
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
