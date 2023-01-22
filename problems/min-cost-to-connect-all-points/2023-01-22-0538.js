// Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/
// Accepted 2023-01-22 05:38 UTC · JavaScript · 8136 ms · 114.9 MB

/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    const numVertices = points.length
    const edges = []
    for (let i = 0; i < points.length - 1; ++i) {
        for (let j = i + 1; j < points.length; ++j) {
            edges.push({ weight: manhattan(points[i], points[j]), points: [points[i], points[j]] })
        }
    }
    edges.sort((a, b) => a.weight - b.weight)
    let cost = 0
    const uf = new UnionFind()
    while (uf.numEdges < numVertices - 1) {
        const { weight, points: [a, b] } = edges.shift()
        if (uf.connected(a.join(','), b.join(','))) continue
        uf.union(a.join(','), b.join(','))
        cost += weight        
    }
    return cost
}

function manhattan(a, b) {
    const [[x1, y1], [x2, y2]] = [a, b]
    return Math.abs(x1 - x2) + Math.abs(y1 - y2)
}

class UnionFind {
    constructor() {
        this.roots = {}
        this.numEdges = 0
    }

    find(x) {
        if (!this.roots.hasOwnProperty(x) || this.roots[x] === x) return x
        this.roots[x] = this.find(this.roots[x])
        return this.roots[x]
    }

    union(x, y) {
        if (!this.roots.hasOwnProperty(x)) this.roots[x] = x
        if (!this.roots.hasOwnProperty(y)) this.roots[y] = y
        const [rootX, rootY] = [this.find(x), this.find(y)]
        if (rootX !== rootY) {
            this.roots[rootX] = rootY
            this.numEdges += 1
        }
    }

    connected(x, y) {
        return this.roots.hasOwnProperty(x) && this.roots.hasOwnProperty(y) && this.find(x) === this.find(y)
    }
}
