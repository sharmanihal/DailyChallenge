class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # If there are no trust relationships and only one person, that person is the judge
        if len(trust) == 0 and n == 1:
            return 1
        
        # set to store the people who trust someone
        manWhoTrustSomeOne = set()
        
        # Dictionary to store the count of people trusted by all
        trustedManByAll = {}
        
        # Iterate through the trust relationships
        for i in trust:
            manWhoTrustSomeOne.add(i[0])
            trustedManByAll[i[1]] = trustedManByAll.get(i[1], 0) + 1
        
        # Initialize candidate for judge
        candidate = 0
        
        # Find the candidate who trusts no one
        for i in range(1, n + 1):
            if i not in manWhoTrustSomeOne:
                candidate = i
        
        # If no candidate found, return -1
        if candidate == 0:
            return -1
        
        # If candidate is not trusted by all or there are not n-1 trust relationships to the candidate
        if candidate not in trustedManByAll or trustedManByAll[candidate] != n - 1:
            return -1
        
        # Return the candidate who satisfies all conditions
        return candidate
