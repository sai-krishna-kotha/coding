# hashmap
k = int(input())
hash_map = {}
string = input()
for s in string:
    hash_map[s] = hash_map.get(s, 0) + 1
for v in hash_map.values():
    if v % k != 0:
        print(-1)
        exit()
base = ''
for c in hash_map.keys():
    base += c * (hash_map[c]//k)
print(f"{base*k}")