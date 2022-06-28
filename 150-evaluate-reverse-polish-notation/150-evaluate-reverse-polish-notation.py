class Solution:
    def check_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

    def evalRPN(self, A):
        stack = deque()
        ans = 0
        for a in A:
            if self.check_int(a):
                stack.append(a)
            elif a == '+':
                a = stack.pop()
                b = stack.pop()
                ans = int(a)+int(b)
                stack.append(ans)
            elif a == '-':
                a = stack.pop()
                b = stack.pop()
                ans = int(b)-int(a)
                stack.append(ans)
            elif a == '*':
                a = stack.pop()
                b = stack.pop()
                ans = int(a)*int(b)
                stack.append(ans)
            elif a == '/':
                a = stack.pop()
                b = stack.pop()
                ans = int(int(b)/int(a))
                stack.append(ans)
        return stack.pop()

        