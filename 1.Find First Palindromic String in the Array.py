
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through each word in the input list
        for i in words:
            # Check if the current word is a palindrome
            if self.checkPali(i):
                # If it is a palindrome, return the word
                return i
        # If no palindrome is found, return an empty string
        return ""
        
    def checkPali(self, word):
        # Initialize pointers at the beginning and end of the word
        i, j = 0, len(word) - 1
        # Iterate while the pointers haven't crossed each other
        while i < j:
            # If characters at the current positions don't match, return False
            if word[i] != word[j]:
                return False
            # Move the pointers towards the center of the word
            i += 1
            j -= 1
        # If the loop completes without returning False, the word is a palindrome, so return True
"""
Explanation:
- The `firstPalindrome` method iterates through each word in the input list `words`.
- For each word, it calls the `checkPali` method to determine if it's a palindrome.
- The `checkPali` method uses two pointers starting from the beginning and end of the word and iterates towards the center.
- If the characters at corresponding positions don't match, it returns `False`, indicating that the word is not a palindrome.
- If the loop completes without returning `False`, it means the word is a palindrome, so it returns `True`.
- If a palindrome is found in the `firstPalindrome` method, it returns the word. Otherwise, it returns an empty string.
"""
