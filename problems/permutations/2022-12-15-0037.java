// Permutations
// https://leetcode.com/problems/permutations/
// Accepted 2022-12-15 00:37 UTC · Java · 0 ms · 42.8 MB

class Solution {
    private List<List<Integer>> output = new ArrayList<>();
    private int[] input;

    public List<List<Integer>> permute(int[] nums) {
        this.input = nums;
        backtrack(0);
        return this.output;
    }

    private void backtrack(int first) {
        if (first == this.input.length) {
            List<Integer> permutation = new ArrayList<>();
            for (int num : this.input) {
                permutation.add(num);
            }
            this.output.add(permutation);
            return;
        }
        for (int i = first; i < this.input.length; ++i) {
            swap(first, i);
            backtrack(first + 1);
            swap(first, i);
        }
    }

    private void swap(int l, int r) {
        int tmp = this.input[l];
        this.input[l] = this.input[r];
        this.input[r] = tmp;
    }
}
