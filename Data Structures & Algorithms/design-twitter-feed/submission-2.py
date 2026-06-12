class Twitter:

    def __init__(self):
        self.followeeMap = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        tweets = []
        self.followeeMap[userId].add(userId)
        for followeeId in self.followeeMap[userId]:
            if self.tweets[followeeId]:
                followee_tweets = self.tweets[followeeId]
                index = len(followee_tweets) - 1
                cnt, tweetId = followee_tweets[index]
                heapq.heappush(tweets, [cnt, tweetId, followeeId, index-1])

        while tweets and len(res) < 10:
            cnt, tweetId, followeeId, index = heapq.heappop(tweets)
            res.append(tweetId)
            if index >= 0:
                followee_tweets = self.tweets[followeeId]
                cnt, tweetId = followee_tweets[index]
                heapq.heappush(tweets, [cnt, tweetId, followeeId, index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)
