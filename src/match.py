import random
import time
from numpy.random import choice

#so far it is not an object, it is only a function repository

def play_possession_by_quarter(game_t_count, quarter_n, poss_time):
    time.sleep(poss_time)
    game_t_count += poss_time
    print(f"A new possession has passed. The possesion has had {poss_time} seconds. The actual time is: {game_t_count}.")
    return game_t_count #not sure if it is necessary to return it

def change_possesion(last_play, possession_Item):
    if last_play == "offensive_rebound":
        return possesion_Item
    possesion_Item = 1 if possesion_Item == 0 else 0
    return possession_Item

#TODO -> it is still  WIP -> maybe the best is to return the "name" of the action is going to happen
def action_by_possesion():
    rand_counter = random.random()
    if rand_counter >= 0 and rand_counter <= 0.70: #Shoot Attempt
        return "field_attempt"
    elif rand_counter > 0.70 and rand_counter <= 0.80: #turnover
        if rand_counter > 0.70 and rand_counter <= 0.75:
            return "only_turnover"
        elif rand_counter > 0.75 and rand_counter <= 0.80:
            return "turnover_+_Steal"
    elif rand_counter > 0.80 and rand_counter <= 1: #fouls
        if rand_counter > 0.80 and rand_counter <= 0.88:
            return "throw_in"
        if rand_counter > 0.88 and rand_counter <= 0.95:
            return "two_FT"
        if rand_counter > 0.95 and rand_counter <= 0.98:
            return "two_+_1_FT"
        if rand_counter > 0.98 and rand_counter <= 1:
            return "three_+_1_FT"

def rebound_result():
    rebound_direction_perc = random.random()
    if rebound_direction_perc < 0.95:
        return "defensive_rebound"
    elif rebound_direction_perc >= 0.95:
        return "offensive_rebound"

def rebound_action(rebound_situation, defending_team, possession_team):
    if rebound_situation == "defensive_rebound":
        name_rebound_player = defending_team.select_random_on_court_player()
        defending_team.roster[name_rebound_player].rebound_made()
        #message
        print(f"{name_rebound_player} of defensive team {defending_team.team_name} has catched a defensive rebound.")

    elif rebound_situation == "offensive_rebound":
        name_rebound_player = possession_team.select_random_on_court_player()
        possession_team.roster[name_rebound_player].rebound_made()
        #message
        print(f"{name_rebound_player} of offensive team {defending_team.team_name} has catched an offensive rebound.")

def type_shoot_weight_selection():
    return choice([2,3], 1, p=[0.65, 0.35])[0]

def change_possession_rebound(rebound_situation, possession_Item):
    if rebound_situation == "defensive_rebound":
        return 1 if possession_Item == 0 else 0 #change possession
    elif rebound_situation == "offensive_rebound":
        return possession_Item #no change is done on possession_Item variable





    



