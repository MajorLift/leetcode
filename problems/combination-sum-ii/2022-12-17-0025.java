// Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/
// Accepted 2022-12-17 00:25 UTC · Java · 3 ms · 42.9 MB

class Solution {
    private List<List<Integer>> output = new ArrayList<>();
    private int[] input;

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        this.input = candidates;
        Arrays.sort(this.input);
        this.backtrack(new ArrayList<>(), 0, target);
        return this.output;
    }

    private void backtrack(List<Integer> path, int start, int remainder) {
        if (remainder == 0) {
            this.output.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < this.input.length; ++i) {
            if (i > start && this.input[i] == this.input[i - 1]) continue;
            if (remainder - this.input[i] >= 0) {
                path.add(this.input[i]);
                this.backtrack(path, i + 1, remainder - this.input[i]);
                path.remove(path.size() - 1);
            }
        }
    }
}
