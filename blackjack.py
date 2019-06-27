from random import shuffle

class Shoe:

    def __init__(self, shoe_size=1):
        self.burn = []
        self.shoe = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]*4 * shoe_size
        
    def shuffle_shoe(self):
        self.shoe = self.shoe + self.burn
        self.burn = []
        shuffle(self.shoe)
        
    def draw_card(self):
        card = self.shoe[0]
        self.shoe[:] = self.shoe[1:]
        self.burn[:] = self.burn+[card]
        return card
        
class Hand:
    
    def __init__(self):
        self.cards = []
        
    def draw_card(self, deck):
        self.cards.append(deck.draw_card())
        
    def evaluate_score(self):
        score = 0
        soft_aces = 0
        self.cardDict = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10}
        for card in self.cards:
            score+=self.cardDict[card]
            if(card == "A"):
                soft_aces += 1
            if(score > 21):
                if(soft_aces > 0):
                    soft_aces -= 1
                    score -= 10
        return score
        
    def is_blackjack(self):
        return (len(self.cards)==2 and self.evaluate_score() == 21)
        
    def pretty_print(self):
        pretty_string = ""
        for card in self.cards:
            pretty_string += card + " "
        pretty_string += "\tScore: " + str(self.evaluate_score())
        print pretty_string
        
        
class Dealer:
    
    def __init__(self, limit=17):
        self.limit = limit
        self.hand = Hand()
        
    def play_turn(self, deck):
        if(self.limit > self.hand.evaluate_score()):
            self.hand.draw_card(deck)
        
    