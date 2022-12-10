# Design Twitter
# https://leetcode.com/problems/design-twitter/
# Accepted 2022-12-10 22:49 UTC · Python · 54 ms · 14.3 MB

class Tweet:
    def __init__(self, tweetId: int, timestamp: int, next_: 'Tweet' = None):
        self.tweetId = tweetId
        self.timestamp = timestamp
        self.next_ = next_

    def __lt__(self, other: 'Tweet') -> bool:
        return self.timestamp > other.timestamp

class User:
    def __init__(self, userId: int, following: set[int] = set(), latestTweet: Tweet | None = None):
        self.userId = userId
        self.following = set([*following, self.userId])
        self.latestTweet = latestTweet

    def follow(self, followeeId: int) -> None:
        self.following.add(followeeId)

    def unfollow(self, followeeId: int) -> None:
        self.following.discard(followeeId)

    def postTweet(self, tweet: Tweet) -> None:
        if self.latestTweet:
            tweet.next_ = self.latestTweet
        self.latestTweet = tweet

    def isEmpty(self) -> bool:
        return self.latestTweet is None

class Twitter:
    def __init__(self):
        self.clock = 0
        self.users = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        newTweet = Tweet(tweetId, self.clock)
        self.users[userId] = self.users.get(userId, User(userId))
        self.users[userId].postTweet(newTweet)
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        pq = [self.users[followeeId].latestTweet for followeeId in self.users[userId].following \
            if followeeId in self.users and not self.users[followeeId].isEmpty()]
        heapq.heapify(pq)
        feed = []
        while pq and len(feed) < 10:
            tweet = heapq.heappop(pq)
            feed.append(tweet.tweetId)
            if tweet.next_:
                tweet = tweet.next_
                heapq.heappush(pq, tweet)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId] = self.users.get(followerId, User(followerId))
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
