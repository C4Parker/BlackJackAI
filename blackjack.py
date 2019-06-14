from random import shuffle

class Shoe:

    def __init__(self, shoe_size=1, deck=["A","2","3","4","5","6","7","8","9","T","J","Q","K"]*4):
        self.burn = []
        self.deck = deck
        self.shoe = deck * shoe_size
        
    def shuffle(self):
        shuffle(self.shoe)
        
    def draw_card(self):
        card = self.shoe[0]
        self.shoe[:] = self.shoe[1:]
        self.burn[:] = self.burn+[card]
        return card
        
        
d = Shoe()
d.shuffle()