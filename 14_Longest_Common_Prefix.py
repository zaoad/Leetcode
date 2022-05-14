from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = None
        for s in strs:
            if common is None:
                common = s
            temp = ""
            for i in range(min(len(common), len(s))):
                if common[i] == s[i]:
                    temp+=s[i]
                else:
                    break
            common = temp
        return common