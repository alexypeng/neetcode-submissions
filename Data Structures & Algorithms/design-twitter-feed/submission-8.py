class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        following.add(userId)
        tweets = []
        res = []


        for user in following:
            tweets.extend(self.tweetMap[user][-10:])
        
        heapq.heapify_max(tweets)
        
        for _ in range(10):
            if tweets:
                tweet = heapq.heappop_max(tweets)
                res.append(tweet[1])
        
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
