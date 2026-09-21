class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                # Pop the second operand first, then the first operand
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # int() performs truncation toward zero in Python 3
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
                
        return stack[0]
