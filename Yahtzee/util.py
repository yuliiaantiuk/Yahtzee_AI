import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee!")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
total_rounds = 2
total_played = 2

def draw_static_stuff(player, rounds):
    roll_txt = font.render('Roll the Dice!', True, white)
    screen.blit(roll_txt, (100, 165))

    rolls_left_txt = font.render('Rolls left this turn: ' + str(player.rolls_left), True, white)
    screen.blit(rolls_left_txt, (15, 15))

    accept_txt = font.render('Accept Turn', True, white)
    screen.blit(accept_txt, (390, 165))

    turns_txt = font.render(str(rounds), True, white)
    screen.blit(turns_txt, (WIDTH - 20, 15))

    player_txt = font.render(player.name, True, white)
    screen.blit(player_txt, (WIDTH - 100, HEIGHT - 40))

    pygame.draw.rect(screen, white, [0, 200, 290, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 200), (WIDTH, 200), 3)
    pygame.draw.line(screen, black, (155, 200), (155, HEIGHT), 3)
    pygame.draw.line(screen, black, (225, 200), (225, HEIGHT), 3)
    pygame.draw.line(screen, black, (290, 200), (290, HEIGHT), 3)

def check_possibilities(possible_lst, numbers_lst):
    possible_lst[0] = True
    possible_lst[1] = True
    possible_lst[2] = True
    possible_lst[3] = True
    possible_lst[4] = True
    possible_lst[5] = True
    possible_lst[12] = True
    max_count = 0

    for i in range (1, 7):
        if numbers_lst.count(i) > max_count:
            max_count = numbers_lst.count(i)

    if max_count >= 3:
        possible_lst[6] = True
        if max_count >= 4:
            possible_lst[7] = True
            if max_count == 5:
                possible_lst[11] = True

    if max_count < 3:
        possible_lst[6] = False
        possible_lst[7] = False
        possible_lst[8] = False
        possible_lst[11] = False
    elif max_count == 3:
        possible_lst[7] = False
        possible_lst[11] = False
        checker = False
        for i in range (len(numbers_lst)):
            if numbers_lst.count(numbers_lst[i]) == 2:
                possible_lst[8] = True
                checker = True
        if not checker:
            possible_lst[8] = False
    elif max_count == 4:
        possible_lst[11] = False

    lowest = 10
    highest = 0
    for i in range(len(numbers_lst)):
        if numbers_lst[i] < lowest:
            lowest = numbers_lst[i]
        if numbers_lst[i] > highest:
            highest = numbers_lst[i]

    if (lowest + 1 in numbers_lst) and (lowest + 2 in numbers_lst) and (lowest + 3 in numbers_lst) and (lowest + 4 in numbers_lst):
        possible_lst[10] = True
    else:
        possible_lst[10] = False

    if ((lowest + 1 in numbers_lst) and (lowest + 2 in numbers_lst) and (lowest + 3 in numbers_lst)) or \
            ((highest - 1 in numbers_lst) and (highest - 2 in numbers_lst) and (highest - 3 in numbers_lst)):
        possible_lst[9] = True
    else:
        possible_lst[9] = False

    return possible_lst

def make_choice(clicked_num, selected_lst, done_lst):
    for i in range(len(selected_lst)):
        selected_lst[i] = False
    if not done_lst[clicked_num]:
        selected_lst[clicked_num] = True
    return selected_lst

def update_game_status(players, rounds, game_over):
    global total_rounds, total_played
    if players >= total_played:
        players = 0
        rounds += 1
    if rounds >= total_rounds:
        game_over = True
    return players, rounds, game_over

def check_scores(selected_choice_lst, numbers_lst, possible_lst, current_score):
    active = 0
    for i in range(len(selected_choice_lst)):
        if selected_choice_lst[i]:
            active = i
    if active == 0:
        current_score = numbers_lst.count(1)
    elif active == 1:
        current_score = numbers_lst.count(2) * 2
    elif active == 2:
        current_score = numbers_lst.count(3) * 3
    elif active == 3:
        current_score = numbers_lst.count(4) * 4
    elif active == 4:
        current_score = numbers_lst.count(5) * 5
    elif active == 5:
        current_score = numbers_lst.count(6) * 6
    elif active == 6 or active == 7:
        if possible_lst[active]:
            current_score = sum(numbers_lst)
        else:
            current_score = 0
    elif active == 8:
        if possible_lst[active]:
            current_score = 25
        else:
            current_score = 0
    elif active == 9:
        if possible_lst[active]:
            current_score = 30
        else:
            current_score = 0
    elif active == 10:
        if possible_lst[active]:
            current_score = 40
        else:
            current_score = 0
    elif active == 11:
        if possible_lst[active]:
            current_score = 50
        else:
            current_score = 0
    elif active == 12:
        current_score = sum(numbers_lst)
    return current_score

def check_totals(score_lst, bonus, player):
    player.totals[0] = score_lst[0] + score_lst[1] + score_lst[2] + score_lst[3] + score_lst[4] + score_lst[5]
    if player.totals[0] >= 63:
        player.totals[1] = 35
    else:
        player.totals[1] = 0
    player.totals[2] = player.totals[0] + player.totals[1]
    if bonus:
        player.totals[3] += 100
    player.totals[4] = score_lst[6] + score_lst[7] + score_lst[8] + score_lst[9] + score_lst[10] + score_lst[11] + score_lst[12] + player.totals[3]
    player.totals[5] = player.totals[2]
    player.totals[6] = player.totals[4] + player.totals[5]




