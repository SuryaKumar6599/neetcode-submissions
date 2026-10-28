class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+","-","*","/"]:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    answer = a+b
                elif token == "-":
                    answer = a-b
                elif token == "*":
                    answer = a*b
                else:
                    answer = int(a/b)
                
                stack.append(answer)
            else:
                stack.append(int(token))

        return stack[-1]