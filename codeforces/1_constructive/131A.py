name = input()
ans = []
def all_caps(word):
    for ch in word:
        if ch < chr(65) or ch > chr(90):
            return False
    return True
             
for word in name.split():
    if (not all_caps(word[0]) and len(word) == 1) or ((not all_caps(word[0])) and len(word) >= 2 and all_caps(word[1:])):
        ans.append(word.title())
    elif all_caps(word):
        ans.append(word.lower())
    else:
        ans.append(word)
print(' '.join(ans))