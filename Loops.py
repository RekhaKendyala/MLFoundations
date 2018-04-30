#While Loop

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())
#print(hand)


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = []

#for news_ticker in headlines[i]:
 #   print(news_ticker.append)
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
for i in headlines:
    news_ticker.append(i)
    if len(news_ticker) == 140:
        print(news_ticker)
       # break

    #i+=1



