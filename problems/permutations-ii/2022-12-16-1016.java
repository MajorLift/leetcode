// Permutations II
// https://leetcode.com/problems/permutations-ii/
// Accepted 2022-12-16 10:16 UTC · Java · 5 ms · 43 MB

class Solution {
    private final List<List<Integer>> output = new ArrayList<>();
    private int[] input;

    public List<List<Integer>> permuteUnique(int[] nums) {
        this.input = nums;
        Arrays.sort(this.input);
        boolean[] used = new boolean[this.input.length];
        Arrays.fill(used, false);
        backtrack(new ArrayList<>(), used);
        return this.output;
    }

    private void backtrack(List<Integer> path, boolean[] used) {
        if (path.size() == this.input.length) {
            this.output.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < this.input.length; ++i) {
            if (used[i] == true || i > 0 && used[i - 1] == true && this.input[i] == this.input[i - 1]) continue;
            boolean[] newUsed = Arrays.copyOf(used, used.length);
            newUsed[i] = true;
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(this.input[i]);
            backtrack(newPath, newUsed);
        }
    }
}
