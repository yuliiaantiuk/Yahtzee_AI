class Player:
    def __init__(self, name):
        self.name = name
        self.roll = False
        self.rolls_left = 3
        self.dice_selected = [False, False, False, False, False]
        self.selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.totals = [0, 0, 0, 0, 0, 0, 0]
        self.clicked = -1
        self.current_score = 0
        self.something_selected = False
        self.bonus_time = False
        self.numbers = [0, 0, 0, 0, 0]