class Solution:
    def minimumLength(self, s: str) -> int:
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                break
            while i<len(s) and s[i]==s[j]:
                i+=1
            while i<len(s) and s[j]==s[i-1]:
                j-=1
        if j-i+1>0:
            return j-i+1
        return 0
