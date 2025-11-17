card = list(map(str, input()))
card_rank, card_suit = card[0], card[1]
cards = list(map(str, input().split()))
flag = False
for i in range(5):
    rank, suit = cards[i][0], cards[i][1]
    if rank == card[0] or suit == card[1]:
        print("YES")
        flag = True
        break
if flag == False:
    print("NO")