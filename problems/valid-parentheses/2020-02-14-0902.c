// Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Accepted 2020-02-14 09:02 UTC · C · 0 ms · 7 MB

// bool isValid(char* s) {
//     int len = strlen(s);
//     if(len%2) return false;
    
//     int limit = len/2;
//     char *stack = malloc(limit);
//     int idx = 0;
    
//     for(int i=0; i<len; ++i){
//         char cur = s[i];
//         if(cur=='(' || cur=='{' || cur=='['){
//             if(idx == limit) return false;
//             stack[idx++] = cur;
//         }else{
//             if(idx == 0) return false;
//             if(cur == '}' && stack[idx-1] == '{' || cur == ']' && stack[idx-1] == '[' || cur == ')' && stack[idx-1] == '('){
//                 idx--;
//             }else{
//                 return false;
//             }
//         }
//     }
    
//     free(stack);
//     return idx==0;
// }

bool isValid(char * s){
    int len = strlen(s);
    if(len % 2 == 1) return false;
    
    int limit = len / 2;
    char* stack = (char*) malloc(sizeof(char) * limit);
    int idx = 0;
    int i = 0;
    
    while(i < len){
        int curr = s[i];
        if(curr == '(' || curr == '{' || curr == '['){
            if(idx == limit) return false;
            stack[idx++] = curr;
            i++;
        }
        else{
            if(idx == 0) return false;
            if(curr == ')' && stack[idx-1] == '(' || \
               curr == '}' && stack[idx-1] == '{' || \
               curr == ']' && stack[idx-1] == '['){
                idx--;
                i++;
            }
            else return false;
        }
    }
    free(stack);
    return idx == 0;
}
