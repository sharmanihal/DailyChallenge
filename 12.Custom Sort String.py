class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a Counter object to count occurrences of characters in s
        hashmap = Counter(s)
        # Initialize an empty string to store the result
        res = ""
        
        # Iterate through each character in the order string
        for i in order:
            # Check if the character exists in the Counter object
            if i in hashmap:
                # Append the character to the result string the number of times it appears in s
                for j in range(hashmap[i]):
                    res += i
                # Remove the character from the Counter object
                del hashmap[i]
        
        # If there are any remaining characters in the Counter object
        if len(hashmap):
            # Iterate through each remaining character
            for i in hashmap:
                # Append the character to the result string the number of times it appears in s
                for j in range(hashmap[i]):
                    res += i
        
        # Return the final result string
        return res
