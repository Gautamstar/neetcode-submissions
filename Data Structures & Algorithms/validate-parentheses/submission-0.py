class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i not in parentheses:
                stack.append(i)
            else:
                if not stack or stack[-1] != parentheses[i]:
                    return False
                stack.pop()
        return not stack