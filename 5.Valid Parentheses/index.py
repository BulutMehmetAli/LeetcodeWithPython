def funct():
    pdict = {'[':']' , '{':'}' , '(':')'}
    express = "()([{([[[{{{}}}]]])}])({})"
    
    stack = []
    
    for ch in express:
        if ch in pdict:
            stack.append(ch)
        else:
            if not stack:
                return False
            value = stack.pop()
            if ch != pdict[value]:
                return False
    return len(stack) == 0
print(funct())