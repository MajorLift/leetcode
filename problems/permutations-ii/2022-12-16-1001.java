// Permutations II
// https://leetcode.com/problems/permutations-ii/
// Accepted 2022-12-16 10:01 UTC · Java · 2 ms · 42.8 MB

class Solution {
    private final List<List<Integer>> output = new ArrayList<>();
    private int[] input;

    public List<List<Integer>> permuteUnique(int[] nums) {
        this.input = nums;
        backtrack(0);
        return this.output;
    }

    private void backtrack(int start) {
        if (start == this.input.length) {
            List<Integer> permutation = new ArrayList<>();
            for (int num : this.input) permutation.add(num);
            this.output.add(permutation);
            return;
        }
        Set<Integer> lookup = new HashSet<>();
        for (int i = start; i < this.input.length; ++i) {
            if (lookup.contains(this.input[i])) continue;
            swap(start, i);
            backtrack(start + 1);
            swap(start, i);
            lookup.add(this.input[i]);
        }
    }

    private void swap(int i, int j) {
        int tmp = this.input[i];
        this.input[i] = this.input[j];
        this.input[j] = tmp;
    }
}
