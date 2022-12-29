// Clone Graph
// https://leetcode.com/problems/clone-graph/
// Accepted 2022-12-29 19:19 UTC · Java · 25 ms · 42.6 MB

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    private Map<Integer, Node> visited = new HashMap<>();
    public Node cloneGraph(Node node) {
        if (node == null) return node;
        if (visited.containsKey(node.val)) return visited.get(node.val);
        Node clone = new Node(node.val);
        visited.put(clone.val, clone);
        for (Node v : node.neighbors) clone.neighbors.add(this.cloneGraph(v));            
        return clone;
    }
}
