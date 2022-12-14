// Combinations
// https://leetcode.com/problems/combinations/
// Accepted 2022-12-14 22:42 UTC · Java · 22 ms · 43.5 MB

class Solution {
    private List<List<Integer>> output = new ArrayList<>();
    private int n;
    private int k;

    public List<List<Integer>> combine(int n, int k) {
        this.n = n;
        this.k = k;
        backtrack(new ArrayList<>(), 1, 0);
        return this.output;
    }

    private void backtrack(List<Integer> path, int start, int count) {
        if (count == this.k) {
            this.output.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i <= this.n; ++i) {
            path.add(i);
            backtrack(path, i + 1, count + 1);
            path.remove(path.size() - 1);
        }
    }
}
