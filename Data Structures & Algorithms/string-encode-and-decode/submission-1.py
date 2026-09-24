class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + "#" + s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            pos = s.find("#", i)
            length = int(s[i:pos])
            word = s[pos + 1 : pos + 1 + length]
            result.append(word)
            i = pos + 1 + length
        return result