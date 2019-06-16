from random import shuffle

class Shoe:

    def __init__(self, shoe_size=1, deck=["A","2","3","4","5","6","7","8","9","T","J","Q","K"]*4):
        self.burn = []
        self.deck = deck
        self.shoe = deck * shoe_size
        self.size = len(deck)
        
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
        soft = True
        hard = True
        cardDict = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10}
        
        for card in self.cards:
            score+=cardDict[card]
            if(card == "A"):
                hard = False
            if(score > 21):
                if(not hard and soft):
                    soft = False
                    score -= 10
        return score
        
    def pretty_print(self):
        pretty_string = ""
        for card in self.cards:
            pretty_string += card + " "
            
        pretty_string += "\tScore: " + str(self.evaluate_score())
        print pretty_string
        

    