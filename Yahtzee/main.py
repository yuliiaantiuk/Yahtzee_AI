import random
from dice import *
from choice import *
from util import *
from player import *
from ai import *
import time

rounds_played = 0
players_played = 0
user = Player("User")
computer = Player("Computer")
players = [user, AI(computer)]
current_player = players[0]
game_over = False

def restart_game():
    global game_over
    global rounds_played
    global players_played
    global user
    global computer
    global players
    global current_player

    user = Player("User")
    computer = Player("Computer")
    players = [user, computer]
    current_player = players[0]

    game_over = False
    rounds_played = 0
    players_played = 0

def draw_game_result():
    winner = None
    if user.totals[-1] > computer.totals[-1]:
        winner = user
    elif computer.totals[-1] > user.totals[-1]:
        winner = computer
    win_txt = font.render(winner.name + "wins! User: " + str(user.totals[-1]) + " Computer: " + str(computer.totals[-1]), True, white)
    screen.blit(win_txt, (310, 230))

if __name__ == '__main__':
    running = True
    while running:
        timer.tick(fps)
        screen.fill(background)

        restart_btn = pygame.draw.rect(screen, black, [1000, 1000, 2000, 3000])

        if game_over:
            restart_btn = pygame.draw.rect(screen, black, [300, 275, 280, 30])
            restart_txt = font.render('Click to restart', True, white)
            screen.blit(restart_txt, (370, 280))
            draw_game_result()

        roll_btn = pygame.draw.rect(screen, black, [10, 160, 280, 30])
        accept_btn = pygame.draw.rect(screen, black, [310, 160, 280, 30])

        draw_static_stuff(current_player, rounds_played)
        die1, die2, die3, die4, die5 = create_and_draw_dice(current_player)
        ones, twos, threes, fours, fives, sixes, upper_total1, upper_bonus, upper_total2, three_kind, four_kind, full_house, small_straight, large_straight, yahtzee, chance, bonus, lower_total1, lower_total2, grand_total = create_and_draw_choice(current_player, user, computer)

        current_player.possible = check_possibilities(current_player.possible, current_player.numbers)
        current_player.current_score = check_scores(current_player.selected_choice, current_player.numbers,
                                                    current_player.possible, current_player.current_score)

        if True in current_player.selected_choice:
            current_player.something_selected = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                die1.check_click(event.pos)
                die2.check_click(event.pos)
                die3.check_click(event.pos)
                die4.check_click(event.pos)
                die5.check_click(event.pos)

                if 0 <= event.pos[0] <= 155:
                    if 200 <= event.pos[1] <= 380 or 470 <= event.pos[1] <= 680:
                        if 200 < event.pos[1] <= 230:
                            current_player.clicked = 0
                        if 230 < event.pos[1] <= 260:
                            current_player.clicked = 1
                        if 260 < event.pos[1] <= 290:
                            current_player.clicked = 2
                        if 290 < event.pos[1] <= 320:
                            current_player.clicked = 3
                        if 320 < event.pos[1] <= 350:
                            current_player.clicked = 4
                        if 350 < event.pos[1] <= 380:
                            current_player.clicked = 5
                        if 470 < event.pos[1] <= 500:
                            current_player.clicked = 6
                        if 500 < event.pos[1] <= 530:
                            current_player.clicked = 7
                        if 530 < event.pos[1] <= 560:
                            current_player.clicked = 8
                        if 560 < event.pos[1] <= 590:
                            current_player.clicked = 9
                        if 590 < event.pos[1] <= 620:
                            current_player.clicked = 10
                        if 620 < event.pos[1] <= 650:
                            current_player.clicked = 11
                        if 650 < event.pos[1] <= 680:
                            current_player.clicked = 12
                        current_player.selected_choice = make_choice(current_player.clicked,
                                                                     current_player.selected_choice,
                                                                     current_player.done)

                if roll_btn.collidepoint(event.pos) and current_player.rolls_left > 0 and current_player == players[0]:
                    current_player.roll = True
                    current_player.rolls_left -= 1

                if accept_btn.collidepoint(
                        event.pos) and current_player.rolls_left < 3 and current_player.something_selected and current_player == players[0]:
                    if current_player.score[11] == 50 and current_player.done[11] and current_player.possible[11]:
                        current_player.bonus_time = True
                    for i in range(len(current_player.selected_choice)):
                        if current_player.selected_choice[i]:
                            current_player.done[i] = True
                            current_player.score[i] = current_player.current_score
                            check_totals(current_player.score, current_player.bonus_time, current_player)
                            current_player.selected_choice[i] = False
                    for i in range(len(current_player.dice_selected)):
                        current_player.dice_selected[i] = False
                    current_player.numbers = [7, 18, 29, 30, 41]
                    current_player.something_selected = False
                    current_player.rolls_left = 3
                    players_played += 1
                    players_played, rounds_played, game_over = update_game_status(players_played, rounds_played, game_over)
                    current_player = players[1]

                if game_over and restart_btn.collidepoint(event.pos):
                    restart_game()

        if current_player == players[0] and current_player.roll:
            for num in range(len(current_player.numbers)):
                if not current_player.dice_selected[num]:
                    current_player.numbers[num] = random.randint(1, 6)
            current_player.roll = False

        if current_player == players[1]:
            current_player.take_turn()
            #виправити малювання
            die1, die2, die3, die4, die5 = create_and_draw_dice(current_player)
            ones, twos, threes, fours, fives, sixes, upper_total1, upper_bonus, upper_total2, three_kind, four_kind, full_house, small_straight, large_straight, yahtzee, chance, bonus, lower_total1, lower_total2, grand_total = create_and_draw_choice(current_player, user, computer)
            current_player = players[0]
            players_played += 1
            players_played, rounds_played, game_over = update_game_status(players_played, rounds_played, game_over)

        pygame.display.flip()
    pygame.quit()
