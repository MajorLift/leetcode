// Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/
// Accepted 2022-01-26 16:51 UTC · JavaScript · 109 ms · 42.9 MB

/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(seats) {
    const distances = new Array(seats.length).fill(0);
    const ones = seats.reduce((acc, curr, i) => {
        if (curr === 1) acc.push(i);
        return acc;
    }, []);
    ones.forEach((e, i) => {
        let [j, k] = [1, 1];
        while (e - j >= 0 && (distances[e - j] === 0 || distances[e - j] > j)) {
            distances[e - j] = j;
            j++;
        }
        while (e + k < seats.length && (i + 1 < ones.length ? e + k < ones[i + 1] : true) && (distances[e + k] === 0 || distances[e + k] > k)) {
            distances[e + k] = k;
            k++;
        }
    });
    // console.log(distances);
    return Math.max(...distances);
};
