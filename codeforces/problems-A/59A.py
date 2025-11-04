name = input()
cap = small = 0
for ch in name:
    if 65 <= ord(ch) <= 90:
        cap += 1
    else:
        small += 1
if cap > small:
    print(name.upper())
else:
    print(name.lower())
    