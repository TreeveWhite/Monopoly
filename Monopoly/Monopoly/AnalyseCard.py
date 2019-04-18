"""
Program to analise contents of a chnace or community card and retrun instructions to cary out.
"""

class AnaliseChance:

    def Analise(card, player):
        amount = ""
        cardSplit = card.split()
        cardArray = list(cardSplit)
        for letter in cardArray:
            if str.isdigit(letter):
                amount += str(letter)
        print(amount)
        print(card)
        if "win" in cardArray:
            player.money += int(amount)
        elif "lose" in cardArray:
            player.moeny -= int(amount)