def is_matched(expression):
    stack = []
    pairDict = {'{':'}', '[':']', '(':')'}
    for brac in expression:
        if brac in pairDict:
            stack.append(brac)
        elif brac in pairDict.values():
            if len(stack) >= 1 and pairDict[stack[-1]] == brac:
                stack.pop()
            else:
                return False
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
