// Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/
// Accepted 2020-03-11 14:27 UTC · Java · 0 ms · 36.3 MB

/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1;
        int right = n;
        while(right - left >= 0){
            int mid = left + (right - left) / 2;
            if(guess(mid) == 0) return mid;
            if(guess(mid) == -1) right = mid - 1;
            if(guess(mid) == 1) left = mid + 1;
        }
        return -1;
    }
}
