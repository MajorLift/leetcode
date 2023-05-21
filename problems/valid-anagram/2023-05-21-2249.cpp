// Valid Anagram
// https://leetcode.com/problems/valid-anagram/
// Accepted 2023-05-21 22:49 UTC · C++ · 8 ms · 7.3 MB

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> cnt;
        for (int i = 0; i < s.length(); ++i) {
            cnt[s[i]]++;
            cnt[t[i]]--;
        }
        for (auto count : cnt) {
            if (count.second) return false;
        }
        return true;
    }
};
