// Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/
// Accepted 2023-05-22 05:53 UTC · C++ · 44 ms · 21.2 MB

class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded = "";
        for (const string &s : strs) {
            encoded += to_string(s.size()) + '#' + s;
        }
        return encoded;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decoded;
        for (int i = 0, n = 0; i < s.size();) {
            n = 0;
            while (isdigit(s[i])) {
                n *= 10;
                n += s[i++] - '0';
            }
            decoded.push_back(s.substr(++i, n));
            i += n;
        }
        return decoded;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
