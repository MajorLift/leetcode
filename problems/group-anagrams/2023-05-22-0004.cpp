// Group Anagrams
// https://leetcode.com/problems/group-anagrams/
// Accepted 2023-05-22 00:04 UTC · C++ · 40 ms · 19 MB

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (const auto& s : strs) {
            mp[strSort(s)].push_back(s);
        }
        vector<vector<string>> anagrams;
        anagrams.reserve(mp.size());
        for (const auto& p : mp) {
            anagrams.push_back(move(p.second));
        }
        return anagrams;
    }
private:
    string strSort(string s) {
        int counter[26] = {0};
        for (const char c : s) {
            counter[c - 'a']++;
        }
        string t;
        for (int c = 0; c < 26; ++c) {
            t += string(counter[c], c + 'a');
        }
        return t;
    }
};
