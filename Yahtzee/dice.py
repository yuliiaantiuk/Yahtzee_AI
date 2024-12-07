import pygame
from util import black, white, screen

black = (0, 0, 0)
class Dice:
    def __init__(self, x_pos, y_pos, num, key, player):
        global dice_selected
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.num = num
        self.key = key
        self.die = ''
        self.selected = player.dice_selected[key]
        self.player = player

    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.num == 1:
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
        if self.num == 2:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 3:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
        if self.num == 4:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 5:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 50, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.num == 6:
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 20], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 20, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 80], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 50], 10)
            pygame.draw.circle(screen, black, [self.x_pos + 80, self.y_pos + 20], 10)
        if self.selected:
            self.die = pygame.draw.rect(screen, (255, 0, 0), [self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if self.player.dice_selected[self.key]:
                self.player.dice_selected[self.key] = False
            elif not self.player.dice_selected[self.key]:
                self.player.dice_selected[self.key] = True

def create_and_draw_dice(current_player):
    die1 = Dice(10, 50, current_player.numbers[0], 0, current_player)
    die2 = Dice(130, 50, current_player.numbers[1], 1, current_player)
    die3 = Dice(250, 50, current_player.numbers[2], 2, current_player)
    die4 = Dice(370, 50, current_player.numbers[3], 3, current_player)
    die5 = Dice(490, 50, current_player.numbers[4], 4, current_player)

    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()

    return die1, die2, die3, die4, die5
