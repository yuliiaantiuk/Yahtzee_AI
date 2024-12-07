import pygame
from util import black, screen, font
class Choice:
    def __init__(self, x_pos, y_pos, text, select, is_possible, is_done, score1, score2):
        global selected_choice
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.is_possible = is_possible
        self.is_done = is_done
        self.score1 = score1
        self.score2 = score2

    def draw(self):
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos), (self.x_pos + 290, self.y_pos), 2)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + 30), (self.x_pos + 290, self.y_pos + 30), 2)

        if not self.is_done:
            if self.is_possible:
                my_text = my_text = font.render(self.text, True, (80, 200, 96))
            elif not self.is_possible:
                my_text = my_text = font.render(self.text, True, (250, 0, 55))
        else:
            my_text = font.render(self.text, True, black)
        if self.select:
            pygame.draw.rect(screen, (20, 35, 30), [self.x_pos, self.y_pos, 155, 30])
        screen.blit(my_text, (self.x_pos + 5, self.y_pos + 10))
        score_text1 = font.render(str(self.score1), True, (0, 0, 255))
        screen.blit(score_text1, (self.x_pos + 165, self.y_pos + 10))
        score_text2 = font.render(str(self.score2), True, (0, 0, 255))
        screen.blit(score_text2, (self.x_pos + 238, self.y_pos + 10))

def create_and_draw_choice(current_player, user, computer):
    ones = Choice(0, 200, '1s', current_player.selected_choice[0], current_player.possible[0],
                  current_player.done[0], user.score[0], computer.score[0])
    twos = Choice(0, 230, '2s', current_player.selected_choice[1], current_player.possible[1],
                  current_player.done[1], user.score[1], computer.score[1])
    threes = Choice(0, 260, '3s', current_player.selected_choice[2], current_player.possible[2],
                    current_player.done[2], user.score[2], computer.score[2])
    fours = Choice(0, 290, '4s', current_player.selected_choice[3], current_player.possible[3],
                   current_player.done[3], user.score[3], computer.score[3])
    fives = Choice(0, 320, '5s', current_player.selected_choice[4], current_player.possible[4],
                   current_player.done[4], user.score[4], computer.score[4])
    sixes = Choice(0, 350, '6s', current_player.selected_choice[5], current_player.possible[5],
                   current_player.done[5], user.score[5], computer.score[5])
    upper_total1 = Choice(0, 380, 'Upper Score', False, False, True, user.totals[0], computer.totals[0])
    upper_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True, user.totals[1], computer.totals[1])
    upper_total2 = Choice(0, 440, 'Upper Total', False, False, True, user.totals[2], computer.totals[2])
    three_kind = Choice(0, 470, '3 of Kind', current_player.selected_choice[6], current_player.possible[6],
                        current_player.done[6], user.score[6], computer.score[6])
    four_kind = Choice(0, 500, '4 of Kind', current_player.selected_choice[7], current_player.possible[7],
                       current_player.done[7], user.score[7], computer.score[7])
    full_house = Choice(00, 530, 'Full House', current_player.selected_choice[8], current_player.possible[8],
                        current_player.done[8], user.score[8], computer.score[8])
    small_straight = Choice(0, 560, 'Sm. Straight', current_player.selected_choice[9], current_player.possible[9],
                            current_player.done[9], user.score[9], computer.score[9])
    large_straight = Choice(0, 590, 'Lg. Straight', current_player.selected_choice[10], current_player.possible[10],
                            current_player.done[10], user.score[10], computer.score[10])
    yahtzee = Choice(0, 620, 'YAHTZEE', current_player.selected_choice[11], current_player.possible[11],
                     current_player.done[11], user.score[11], computer.score[11])
    chance = Choice(0, 650, 'Chance', current_player.selected_choice[12], current_player.possible[12],
                    current_player.done[12], user.score[12], computer.score[12])
    bonus = Choice(0, 680, 'YAHTZEE Bonus', False, False, True, user.totals[3], computer.totals[3])
    lower_total1 = Choice(0, 710, 'Lower Total', False, False, True, user.totals[4], computer.totals[4])
    lower_total2 = Choice(0, 740, 'Upper Total', False, False, True, user.totals[5], computer.totals[5])
    grand_total = Choice(0, 770, 'Grand Total', False, False, True, user.totals[6], computer.totals[6])

    ones.draw()
    twos.draw()
    threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    upper_total1.draw()
    upper_bonus.draw()
    upper_total2.draw()
    three_kind.draw()
    four_kind.draw()
    full_house.draw()
    small_straight.draw()
    large_straight.draw()
    yahtzee.draw()
    chance.draw()
    bonus.draw()
    lower_total1.draw()
    lower_total2.draw()
    grand_total.draw()

    return ones, twos, threes, fours, fives, sixes, upper_total1, upper_bonus, upper_total2, three_kind, four_kind, full_house, small_straight, large_straight, yahtzee, chance, bonus, lower_total1, lower_total2, grand_total
