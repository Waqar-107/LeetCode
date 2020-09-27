class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {}
        self.cnt = 1
    

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
            
        self.posts[userId].insert(0, (tweetId, self.cnt))
        self.cnt += 1
        
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop()
            
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        
        if userId in self.posts:
            for p in self.posts[userId]:
                ans.append(p)
        
        if userId in self.following:
            for f in self.following[userId]:
                if f in self.posts:
                    for p in self.posts[f]:
                        ans.append(p)
        
        ans.sort(key = lambda x : x[1], reverse=True)
        
        actual_ans = []
        for i in range(min(10, len(ans))):
            actual_ans.append(ans[i][0])
        
        return actual_ans
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
