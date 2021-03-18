"""
535. Encode and Decode TinyURL

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""

class Codec:

    def __init__(self):
        from collections import defaultdict
        self.hash = defaultdict(int)
        self.backhash = dict()
        self.idx = 0
        self.base = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hash[longUrl] = self.idx
        self.backhash[self.idx] = longUrl
        self.idx += 1

        return self.base + str(self.hash[longUrl])


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idx = shortUrl.split('/')[-1]
        return self.backhash[int(idx)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

"""
Runtime: 36 ms, faster than 52.10% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 14 MB, less than 99.00% of Python3 online submissions for Encode and Decode TinyURL.
"""
