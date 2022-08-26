from deck import Deck


class Player:
    def __init__(self):
        self.hand = []
        self.score = []

    def score_count(self):
        score = [0]
        ace_count = 0
        for item in self.hand:
            score[0] += Deck.value_worth.get(item[0])
            if item[0] == "A":
                ace_count += 1
        if ace_count == 1:
            score.append(score[0] + 10)
        if ace_count == 2:
            score.append(score[0] + 10)
            score.append(score[0] + 20)
        if ace_count == 3:
            score.append(score[0] + 10)
            score.append(score[0] + 20)
            score.append(score[0] + 30)
        if ace_count == 4:
            score.append(score[0] + 10)
            score.append(score[0] + 20)
            score.append(score[0] + 30)
            score.append(score[0] + 40)
        self.score = [item for item in score if item <= 21]

    def check_for_blackjack(self):
        if 21 in self.score:
            return True

    def check_for_bust(self):
        if len(self.score) == 0:
            return True

    def run_dealer(self, this_deck):
        self.score_count()
        while True:
            if len(self.score) != 0 and max(self.score) < 17:
                self.hand.append(this_deck.deck[-1])
                this_deck.deck = this_deck.deck[:-1]
                self.score_count()
            else:
                break

    def hit_question(self, this_deck):
        while True:
            hit = input(f'Would you like to hit?: ')
            if "yes" in hit.lower() or hit.lower() == "":
                self.hand.append(this_deck.deck[-1])
                this_deck.deck = this_deck.deck[:-1]
                return True
            elif "no" in hit.lower() or hit.lower() == "x":
                return False
            else:
                print(f'Please enter either "Yes"/<enter> or "No"/"x"')

    @staticmethod
    def start_question(wallet):
        while True:
            start_response = input(f'You have ${wallet}. Would you like to play?: ')
            if "yes" in start_response.lower() or start_response.lower() == "":
                play = True
                return play
            elif "no" in start_response.lower() or start_response.lower() == "x":
                play = False
                return play
            else:
                print(f'Please enter either "Yes"/<enter> or "No"/"x"')

    @staticmethod
    def keep_playing(wallet):
        while True:
            if wallet == 0:
                print(f'The game is over. You lost all your money!')
                return False
            cont_response = input(f'You have ${wallet} remaining, would you like to play again? ')
            if "yes" in cont_response.lower() or cont_response.lower() == "":
                print("Ok!")
                return True
            elif "no" in cont_response.lower() or cont_response.lower() == "x":
                print(f'The game is over. You finished with ${wallet}!')
                return False
            else:
                print(f'Please enter either "Yes"/<enter> or "No"/"x"')

    @staticmethod
    def bet_question(wallet):
        while True:
            bet = input(f'Place your bet: ')
            if not bet.isdigit():
                print(f"Sorry, please place a bet between $1 and ${wallet}. The table only accepts bets in dollar increments.")
            elif int(bet) <= wallet and int(bet) > 0:
                return int(bet)
            else:
                print(f"Sorry, please place a bet between $1 and ${wallet}. The table only accepts bets in dollar increments.")
