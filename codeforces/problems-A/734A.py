n = int(input())
games = input()
from collections import Counter
freq = Counter(games)
if freq['A'] > freq['D']:
    print("Anton")
elif freq['A'] < freq['D']:
    print("Danik")
else:
    print("Friendship")