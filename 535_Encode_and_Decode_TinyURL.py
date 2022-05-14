class Codec:
    def __init__(self):
        self.count = 1
        self.dict = dict()
        self.base = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.base + str(self.count)
        self.dict[key] = longUrl
        self.count += 1
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dict[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))