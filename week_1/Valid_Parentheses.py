class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"[":"]", "{":"}", "(":")"}
        for char in s:
            if char in dict:
                stack.append(char)
            if char in dict.values():
                if not stack:
                    return False
                if dict[stack.pop()] != char:
                    return False
                    
        if stack:
            return False
        else:
            return True
