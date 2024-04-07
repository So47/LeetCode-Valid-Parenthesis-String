class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open, max_open = 0, 0
    
        for char in s:
            if char == '(':
                min_open, max_open = min_open + 1, max_open + 1
            elif char == ')':
                if min_open > 0:
                    min_open -= 1
                max_open -= 1
                if max_open < 0:  # If there are more close parentheses than open, invalid
                    return False
            else:  # Treat '*' as possible open or close parentheses
                if min_open > 0:
                    min_open -= 1
                max_open += 1
        
        return min_open == 0  # Check if all open parentheses can be matched

        
