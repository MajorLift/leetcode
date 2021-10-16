// Container With Most Water
// https://leetcode.com/problems/container-with-most-water/
// Accepted 2021-10-16 07:06 UTC · JavaScript · 80 ms · 48.3 MB

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
//     let maxArea = 0;
//     for (let i = 0; i < height.length; i += 1) {
//         for (let j = 0; j < height.length; j += 1) {
//             if (height[j] <= height[i] && height[j] * Math.abs(j - i) > maxArea) {
//                 maxArea = height[j] * Math.abs(j - i);
//             }
//         }
        
//     }
//     return maxArea;
    let maxArea = 0;
    let [left, right] = [0, height.length - 1];
    while (left < right) {
        const area = (right - left) * Math.min(height[left], height[right]);
        if (area > maxArea) maxArea = area;
        if (height[left] < height[right]) left++;
        else right--;
    }
    return maxArea;
};
