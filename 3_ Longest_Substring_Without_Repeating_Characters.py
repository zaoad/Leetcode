class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        arry = [-1] * 10000
        start=0
        max=0
        for i in range(0,len(s)):
            # print('first',i,start,max)
            if(arry[ord(s[i])]!=-1 and arry[ord(s[i])]>=start):
                # print('secon',i,start,max)
                if(i-start>max):
                    max=i-start
                start=arry[ord(s[i])]+1
                arry[ord(s[i])]=i
                continue
            arry[ord(s[i])]=i
       # print('third',i,start,max)
        if(i-start+1>max):
            max=i-start+1
        return max
