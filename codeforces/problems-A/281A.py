name = list(input())
first_char = name[0]
if 97 <= ord(first_char) <= 122:
    name[0] = chr(ord(first_char)-32)
print(''.join(name))