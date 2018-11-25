// Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/
// Accepted 2018-11-25 12:30 UTC · Java · 35 ms · N/A

class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> parsed = new HashSet();
        for(String email: emails) {
            int i = email.indexOf('@');
            String local = email.substring(0,i);
            String rest = email.substring(i);
            
            if(local.contains("+")) {
                int j = local.indexOf('+');
                local = local.substring(0,j);
            }
            while(true) {
                if(local.contains(".")) local = local.replace(".", "");
                else break;
            }
            parsed.add(local + rest);
        }
        return parsed.size();
    }
}
