// Design Twitter
// https://leetcode.com/problems/design-twitter/
// Accepted 2022-12-11 06:48 UTC · Java · 16 ms · 42.1 MB

class Tweet {
    public int tweetId;
    public int timestamp;
    public Tweet next;

    public Tweet(int tweetId, int timestamp, Tweet next) {
        this.tweetId = tweetId;
        this.timestamp = timestamp;
        this.next = next;
    }
}

class TweetComparator implements Comparator<Tweet> {
    public int compare(Tweet t1, Tweet t2) {
        return t2.timestamp - t1.timestamp;
    }
}


class User {
    private int userId;
    public Set<Integer> following;
    public Tweet latestTweet;

    public User(int userId, HashSet<Integer> following, Tweet latestTweet) {
        this.userId = userId;
        this.following = following;
        this.latestTweet = latestTweet;
    }

    public void follow(int followeeId) {
        this.following.add(followeeId);
    }

    public void unfollow(int followeeId) {
        if (this.following.contains(followeeId)) this.following.remove(followeeId);
    }

    public void postTweet(Tweet tweet) {
        if (this.latestTweet != null) tweet.next = this.latestTweet;
        this.latestTweet = tweet;
    }

    public boolean isEmpty() {
        return this.latestTweet == null;
    }
}


class Twitter {
    private int clock;
    private Map<Integer, User> users;

    public Twitter() {
        this.clock = 0;
        this.users = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        Tweet newTweet = new Tweet(tweetId, this.clock++, null);
        this.users.putIfAbsent(userId, new User(userId, new HashSet<>(Arrays.asList(userId)), null));
        this.users.get(userId).postTweet(newTweet);
    }
    
    public List<Integer> getNewsFeed(int userId) {
        if (!this.users.containsKey(userId)) return new ArrayList<>();

        Queue<Tweet> pq = new PriorityQueue<Tweet>(new TweetComparator());
        for (int followeeId : this.users.get(userId).following) {
            if (this.users.containsKey(followeeId) && !this.users.get(followeeId).isEmpty()) {
                pq.add(this.users.get(followeeId).latestTweet);
            }
        }

        List<Integer> feed = new ArrayList<>();
        while (!pq.isEmpty() && feed.size() < 10) {
            Tweet tweet = pq.poll();
            feed.add(tweet.tweetId);
            if (tweet.next != null) {
                tweet = tweet.next;
                pq.add(tweet);
            }
        }
        return feed;
    }
    
    public void follow(int followerId, int followeeId) {
        this.users.putIfAbsent(followerId, new User(followerId, new HashSet<>(Arrays.asList(followerId)), null));
        this.users.get(followerId).follow(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        this.users.get(followerId).unfollow(followeeId);
    }
}


/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
