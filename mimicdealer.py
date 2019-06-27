from blackjack import *

shoe = Shoe(6)
shoe.shuffle_shoe()

balance = 0
min_bet = 1
max_bet = 1
number_simulations = 100
reshuffle_size = 0.5


for i in range (0,number_simulations):
    
    bet = max_bet

    # shuffle burn cards back into shoe
    if(len(shoe.shoe) < reshuffle_size * len(shoe.shoe + shoe.burn)):
        shoe.shuffle_shoe()
        print "reshuffling"
        
    # begin new hand
    dealer = Dealer()
    player = Hand()
    player.draw_card(shoe)
    dealer.play_turn(shoe)
    player.draw_card(shoe)

    #print "Player: " + player.pretty_string()
    #print "Dealer: " + dealer.hand.pretty_string()

    # strategy
    while(player.evaluate_score() < 17):
        player.draw_card(shoe)
        #player.pretty_print()

    # dealer turn
    while(dealer.hand.evaluate_score() < dealer.limit):
        dealer.play_turn(shoe)
        #dealer.hand.pretty_print()
    
    print "Player: " + player.pretty_string()
    print "Dealer: " + dealer.hand.pretty_string()
    
    # determine winner
    if(player.is_blackjack()):
        balance += 1.5 * bet
    elif(compare_hands(player, dealer.hand) < 0):
        balance += bet
    elif(compare_hands(player, dealer.hand) > 0):
        balance -= bet
        
print balance
    