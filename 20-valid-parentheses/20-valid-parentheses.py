class Solution:
    def isValid(self, A: str) -> bool:
        stack = deque()
        for a in A:
            if a == '(' or a == '{' or a == '[':
                stack.append(a)
            elif len(stack) == 0:
                return 0
            elif a == ')':
                if stack.pop() != '(':
                    return 0
            elif a == '}':
                if stack.pop() != '{':
                    return 0             
            elif a == ']':
                if stack.pop() != '[':
                    return 0
        return 1 if len(stack) == 0 else 0