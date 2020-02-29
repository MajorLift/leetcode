// Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/
// Accepted 2020-02-29 10:44 UTC · C · 4 ms · 5.6 MB

char* substr(char* s, int a, int b){
    char* ret = (char*) malloc(sizeof(char) * (b - a + 1));
    int i = -1;
    while(++i < b - a) ret[i] = s[a + i];
    ret[i] = '\0';
    return ret;
}

char * longestCommonPrefix(char ** strs, int strsSize){
    if(strsSize == 0) return "";
    int j = 0;   
    while(strs[0][j] != '\0'){
        int i = 0;
        while(++i < strsSize){
            if(strs[i][j] == '\0') break;
            if(strs[i - 1][j] != strs[i][j]) break;
        }
        if(i == strsSize) j++;
        else break;
    }
    if(j == 0) return "";
    return substr(strs[0], 0, j);
}
