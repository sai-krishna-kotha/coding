name = input()
ans = ''
for i in range(len(name)):
    ele = name[i]
    # vowels
    if name[i] in ['a', 'e', 'i', 'o', 'u', 'y', 'A','E','I','O','U','Y']:
        continue
    # lower
    elif 65 <= ord(ele) <= 90:
        ans += f".{chr(ord(ele)+32)}"
    # consonents
    else:
        ans += f".{ele}"
print(ans)