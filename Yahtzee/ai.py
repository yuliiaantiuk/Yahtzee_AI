from util import *
import random
from player import *
from dice import *
from choice import *

class AI(Player):

    def take_turn(self):
        while self.rolls_left > 0:
            # Roll dice
            for i in range(len(self.numbers)):
                if not self.dice_selected[i]:
                    self.numbers[i] = random.randint(1, 6)
            self.rolls_left -= 1
            die1, die2, die3, die4, die5 = create_and_draw_dice(self)

            # Evaluate possibilities
            self.possible = check_possibilities(self.possible, self.numbers)
            best_choice = self.choose_best_option()

            if best_choice is not None:
                self.clicked = best_choice
                self.selected_choice = make_choice(best_choice, self.selected_choice, self.done)
                break

        # Finalize the choice
        if self.selected_choice:
            for i in range(len(self.selected_choice)):
                if self.selected_choice[i]:
                    self.done[i] = True
                    self.score[i] = check_scores(self.selected_choice, self.numbers,
                                                        self.possible, self.current_score)
                    check_totals(self.score, self.bonus_time, self)
                    self.selected_choice[i] = False
            self.rolls_left = 3
            self.dice_selected = [False] * len(self.dice_selected)

    def choose_best_option(self):
        # Find the best scoring category that's possible
        best_choice = None
        best_score = 0
        for i in range(len(self.possible)):
            if self.possible[i] and not self.done[i]:
                score = check_scores([True if j == i else False for j in range(len(self.possible))],
                                     self.numbers, self.possible, self.current_score)
                if score > best_score:
                    best_score = score
                    best_choice = i
        return best_choice
