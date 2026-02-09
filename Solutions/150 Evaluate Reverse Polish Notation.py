class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #  meet every "2 operand 1 operator" do calculation
        stack = []
        operators = {'+','-','*','/'}
        for t in tokens:
            if t in operators:
                # a +-*/ b , and it guatantees valid expression
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    c = a+b
                elif t == '-':
                    c = a-b
                elif t == '*':
                    c = a*b
                else:
                    c = int(a/b)
                stack.append(c)
            else:
                stack.append(int(t))
        
        # result will be 1 left
        return stack.pop()
        