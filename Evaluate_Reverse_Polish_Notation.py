#stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for c in tokens:
            if c=="+":
                stack.append(stack.pop()+stack.pop())
            elif c=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[0]

#recursions
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token=tokens.pop()
            if token not in "+-*/":
                return int(token)

            r=dfs()
            l=dfs()

            if token=='+':
                return l+r
            elif token=='-':
                return l-r
            elif token=='*':
                return l*r
            elif token=='/':
                return int(l/r)

        return dfs()