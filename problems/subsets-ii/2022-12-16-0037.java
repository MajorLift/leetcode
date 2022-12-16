// Subsets II
// https://leetcode.com/problems/subsets-ii/
// Accepted 2022-12-16 00:37 UTC · Java · 1 ms · 42.4 MB

class Solution {
    private List<List<Integer>> output = new ArrayList<>();
    private int[] input;

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        this.input = nums;
        Arrays.sort(this.input);
        backtrack(new ArrayList<>(), 0);
        return this.output;
    }

    private void backtrack(List<Integer> path, int start) {
        this.output.add(path);
        for (int i = start; i < this.input.length; ++i) {
            if (i > start && this.input[i] == this.input[i - 1]) continue;
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(this.input[i]);
            backtrack(newPath, i + 1);
        }
    }
}
