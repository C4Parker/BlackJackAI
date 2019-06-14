from blackjack import *

d = Shoe()
for i in range (1,10):
    d.draw_card()
    
print d.shoe
print d.burn

d.shuffle_shoe()

print d.shoe
print d.burn