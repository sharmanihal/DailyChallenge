class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # Sort the tokens array
        
        i, j = 0, len(tokens) - 1  # Initialize two pointers
        
        score = 0  # Initialize the score
        maxScore = 0  # Initialize the maximum score
        
        while i <= j:  # Iterate until the two pointers meet or cross each other
            if not score and power >= tokens[i]:  # If score is zero and power is sufficient to play token i
                power -= tokens[i]  # Reduce power
                score += 1  # Increase score
                maxScore = max(maxScore, score)  # Update maxScore
                i += 1  # Move to the next token
                
            elif score and tokens[i] > power:  # If score is non-zero and power is not sufficient to play token i
                score -= 1  # Decrease score
                power += tokens[j]  # Gain power by playing token j
                j -= 1  # Move to the previous token
                
            elif score:  # If score is non-zero
                score += 1  # Increase score
                maxScore = max(maxScore, score)  # Update maxScore
                power -= tokens[i]  # Reduce power
                i += 1  # Move to the next token
                
            else:  # If score is zero and power is not sufficient to play token i
                i += 1  # Skip token i
            
        return maxScore  # Return the maximum score achieved

"""
Explanation:
- It first sorts the tokens array in non-decreasing order.
- Two pointers `i` and `j` are initialized at the beginning and end of the array respectively.
- The function maintains a `score` variable to keep track of the current score and a `maxScore` variable to store the maximum score achieved so far.
- It iterates through the array using the two pointers and performs the following operations:
  - If the score is zero and the current power is sufficient to play the token at index `i`, the function plays the token face-up, increasing the score by 1 and reducing the power.
  - If the score is non-zero and the current power is not sufficient to play the token at index `i`, the function plays the token `j` face-down, decreasing the score by 1 and gaining power.
  - If the score is non-zero and the current power is sufficient to play the token at index `i`, the function plays the token face-up, increasing the score by 1 and reducing the power.
  - If the score is zero and the current power is not sufficient to play the token at index `i`, the function skips the token.
- The function returns the maximum score achieved after playing any number of tokens.
"""

