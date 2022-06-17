# Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/
# Accepted 2022-06-17 21:33 UTC · Python · 79 ms · 14.2 MB

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for [username, domain] in list(map(lambda x: x.split('@'), emails)):
            username = username[:username.find('+')] if username.find('+') > -1 else username
            username = re.sub('\.', '', username)
            email_set.add(username + '@' + domain)
        print(email_set)
        return len(email_set)
