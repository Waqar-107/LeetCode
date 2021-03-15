class Codec:
    def __init__(self):
        self.id = 1
        self.dict = {}
        
    def encode(self, longUrl: str) -> str:
        self.dict[str(self.id)] = longUrl
        ret = self.id
        self.id += 1
        return str(ret)
        

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.dict:
            return self.dict[shortUrl]
        
        return ""
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
