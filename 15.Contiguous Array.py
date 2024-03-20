class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap={0:0}
        count=0
        maxlength=0
        for ind,val in enumerate(nums,1):
            if val==0:
                count-=1
            else:
                count+=1
            if count in hashmap:
                maxlength=max(maxlength,ind-hashmap[count])
            else:
                hashmap[count]=ind
        return maxlength
