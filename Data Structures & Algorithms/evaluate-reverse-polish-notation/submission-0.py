class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if stack and token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif stack and token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif stack and token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2*num1)
            elif stack and token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(token))  
        return stack[-1]      