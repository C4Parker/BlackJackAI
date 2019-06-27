from blackjack import *


shoe = Shoe()
shoe.shuffle_shoe()

player = Hand()
player.draw_card(shoe)
player.draw_card(shoe)

print player.cards
print shoe.burn
print shoe.shoe

player.pretty_print()

print player.is_blackjack()

dealer = Dealer()

while(dealer.hand.evaluate_score() < dealer.limit):
    dealer.play_turn(shoe)
    dealer.hand.pretty_print()