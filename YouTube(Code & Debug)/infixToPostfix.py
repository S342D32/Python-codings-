
class Solution:
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return -1

    def InfixtoPostfix(self, s):
        stack = []
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)

            elif char == "(":
                stack.append(char)

            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                if stack:
                    stack.pop()

            else:
                while (stack and stack[-1] != "(" and
                       (self.precedence(stack[-1]) >
                        self.precedence(char) or
                        (self.precedence(stack[-1]) ==
                         self.precedence(char) and char != "^"))):
                    result.append(stack.pop())

                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result)

# Time Complexity = O(N); Space Complexity = O(N).