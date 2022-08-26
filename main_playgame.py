'''
Main
This module allows a user to play the game of Blackjack
-
Developed by PCV on 8/2022 for practicing fundamental python skills
'''
from player import Player
from deck import Deck


# start
wallet = 500
play = Player.start_question(wallet)

# run the game
while play:
    # loop toggles
    round = True
    hit = True

    # place a bet
    bet = Player.bet_question(wallet)

    # create instances for the two players
    dealer = Player()
    player = Player()

    # start a new deck, shuffle, and deal
    this_deck = Deck()
    this_deck.shuffle_deck()
    player.hand, dealer.hand = this_deck.deal(player.hand, dealer.hand)
    player.score_count()
    print(f'Dealer\'s hand:     {[dealer.hand[0], "XX"]}')
    print(f'Player\'s hand:     {player.hand}')
    print(f' and score(s):     {player.score}')

    # check for a blackjack
    if player.check_for_blackjack():
        print("Blackjack! You won!")
        wallet += 1.5 * bet
        hit = False
        round = False

    # player's turn to hit
    while hit:
        hit = player.hit_question(this_deck)
        if hit:
            player.score_count()
            print(f'Dealer\'s hand:     {[dealer.hand[0], "XX"]}')
            print(f'Player\'s hand:     {player.hand}')
            print(f' and score(s):     {player.score}')

            # check for a blackjack or a bust
            if player.check_for_blackjack():
                print("Blackjack! You won!")
                wallet += 1.5 * bet
                hit = False
                round = False
            if player.check_for_bust():
                print("That's a bust! You lost!")
                wallet -= bet
                hit = False
                round = False
        else:
            hit = False
            round = True

    # if the round is still active: run the dealer and compare player and dealer score
    if round:
        # dealer's turn to hit
        dealer.run_dealer(this_deck)
        print(f'Dealer\'s hand:     {dealer.hand}')

        #compare scores
        if len(dealer.score) == 0 or max(dealer.score) < max(player.score):
            print("You won!")
            wallet += bet
            pass
        elif max(dealer.score) == max(player.score):
            print("That's a draw")
            pass
        else:
            print("Sorry, you lost!")
            wallet -= bet
            pass

    # play again?
    play = Player.keep_playing(wallet)
