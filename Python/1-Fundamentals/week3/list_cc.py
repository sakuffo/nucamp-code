import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    choice = input("Press enter to pick a card, or Q the nenter to quit: ")
    if choice.lower() == "q":
        break
    elif diamonds == []:
        print("There are no more cards to pick.")
    else:
        card = diamonds.pop(random.randint(0, len(diamonds) - 1))
        hand.append(card)
    print("Your hand:", hand)
    print("Remaining cards:", diamonds)
