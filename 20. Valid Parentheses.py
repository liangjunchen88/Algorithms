class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == None:
            return True
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            elif p ==')':
                if stack!=[] and stack[len(stack)-1] == '(':
                    stack.pop()
                else:
                    return False
            elif p =='}':
                if stack!=[] and stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
            elif p ==']':
                if stack!=[] and stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False


# if __name__ == '__main__':
#     S = input()
#     print(Solution().isValid(S))