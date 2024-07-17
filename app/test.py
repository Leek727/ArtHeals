
cards = [1,2,3,4,5]
def move_card(index, direction):
    """0 is down, 1 is up"""
    global cards
    card = cards.pop(index)

    card_index = 
    # get desired index
    if direction:
        index -= 1
    else:
        index += 1

    # check bounds
    if index < 0:
        print("index < 0")
        cards.insert(0, card)
        return 0

    if index > len(cards):
        print("index > lencards")
        cards.append(card)
        return 0

    # move card
    cards.insert(index, card)

while True:
    index = int(input("Select index: "))
    direction = input("up or down?: ")
    d = 0
    if direction == "up":
        d  = 1

    move_card(index, d)
    print(cards)