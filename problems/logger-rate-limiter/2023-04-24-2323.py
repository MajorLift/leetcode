# Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/
# Accepted 2023-04-24 23:23 UTC · Python · 156 ms · 20.8 MB

class Logger:

    def __init__(self):
        self.lastseen = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lastseen \
            or timestamp >= self.lastseen[message] + 10:
            self.lastseen[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
