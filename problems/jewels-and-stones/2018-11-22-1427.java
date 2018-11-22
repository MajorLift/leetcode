// Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/
// Accepted 2018-11-22 14:27 UTC · Java · 8 ms · N/A

class Solution {
    private int count;
    public int numJewelsInStones(String J, String S) {
        for(int i=0; i<J.length(); ++i) {
            for(int j=0; j<S.length(); ++j) {
                if(J.charAt(i) == S.charAt(j)) count++;
            }
        }
        return count;
    }
}
