// Detect Squares
// https://leetcode.com/problems/detect-squares/
// Accepted 2023-04-20 22:33 UTC · JavaScript · 706 ms · 54.6 MB

var DetectSquares = function() {
    this.points = {}
};

/** 
 * @param {number[]} point
 * @return {void}
 */
DetectSquares.prototype.add = function(point) {
    const [x, y] = point
    this.points[`${x},${y}`] = (this.points[`${x},${y}`] ?? 0) + 1
};

/** 
 * @param {number[]} point
 * @return {number}
 */
DetectSquares.prototype.count = function(point) {
    const [x0, y0] = point
    let ans = 0
    for (const coord of Object.keys(this.points)) {
        const [x, y] = coord.split(',').map((e) => parseInt(e))
        if (Math.abs(x - x0) == Math.abs(y - y0) && Math.abs(x - x0) > 0) {
            ans += this.points[`${x},${y}`] 
                * (this.points[`${x0},${y}`] ?? 0)
                * (this.points[`${x},${y0}`] ?? 0)
        }
    }
    return ans
};

/** 
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
