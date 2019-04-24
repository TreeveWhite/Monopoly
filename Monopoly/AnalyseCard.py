"""
Program to analise contents of a chnace or community card and retrun instructions to cary out.
"""

class AnaliseChance:

    def Analise(card):
        amount = ""
        cardSplit = card.split()
        cardArray = list(cardSplit)
        for word in cardArray:
            for letter in word:
                if str.isdigit(letter):
                    amount += str(letter)
        if "win" in cardArray:
            money = int(amount)
        elif "lose" in cardArray:
            money = int(amount) * -1
        return money

    def doCardAction(self, player, amount):
        player.money += int(amount)