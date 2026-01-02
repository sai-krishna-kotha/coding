def isValid(self, s: str) -> bool:
    dici = {'(':')', '[':']', '{':'}'}
    stack = []
    for ch in s:
        if ch in dici:
            stack.append(ch)
        elif not stack or dici[stack.pop()] != ch:
            return False
    return False if stack else True