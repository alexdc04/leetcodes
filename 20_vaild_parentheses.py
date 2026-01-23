class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_stack = list()

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                bracket_stack.append(ch)
            elif ch == ')':
                if bracket_stack and bracket_stack[-1] == '(':
                    bracket_stack.pop()
                else:
                    return False
            elif ch == ']':
                if bracket_stack and bracket_stack[-1] == '[':
                    bracket_stack.pop()
                else:
                    return False
            else:
                if bracket_stack and bracket_stack[-1] == '{':
                    bracket_stack.pop()
                else:
                    return False
            
        if bracket_stack: 
            return False
        else:
            return True

# NOTE: hashmaps can be used as the parentheses are in pairs
