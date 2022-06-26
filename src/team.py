from player import Player
import random
from numpy.random import choice

class Team:
    def __init__(self, ID_Team, team_name, is_local_team, team_conference):    
    #ID_player, name, fga_1_average, fga_2_average, fga_3_average):
        self.ID_Team = ID_Team
        self.team_name = team_name
        self.is_local_team = is_local_team
        self.team_conference = team_conference
        self.roster = {}

    #TO DO Second round-> add coach, add stadium (with its location), ...

    def add_player_to_roster(self, player):
        self.roster[player.name] = player

    #TODO -> CHECK IF IT WORKS.
    def update_seconds_played(self, possession_seconds):
        for player_name in self.roster.keys():
            if self.roster[player_name].on_court == True:
                self.roster[player_name].add_seconds_played(possession_seconds)
    
    #it has been tested, but it is important to remember that the player has to be specified
    #the fact that has to be specified is good, because we will use it to change a player when a player is fouled out.

    def change_on_court_player(self, player_out): #the argument is the player itself
        #First we check if there are available players in the same position and in general
        position_available_players = []
        general_available_players = []
        for player_name in self.roster.keys():
            if (self.roster[player_name].on_court == False) and \
               (self.roster[player_name].fouled_out == False):
               
               general_available_players.append(self.roster[player_name])  #all the players that can play

               if (self.roster[player_name].position == player_out.position):
                   position_available_players.append(self.roster[player_name])  #the players that can play in its position               

        #variable to store if there are available players in the same position       
        there_are_available_players = False if len(position_available_players) == 0 else True
        #decide which ls to use
        ls_to_use = position_available_players if there_are_available_players == True else general_available_players
        
        #Let's use the player's functions to do "the change"
        player_out.court_out()

        player_in = random.choice(ls_to_use)
        player_in.court_in()
        
        #message
        print(f"{player_out} has been changed by {player_in}.")

    
    def attack_player(self):
        #creamos una lista con los jugadores "on_court == True"
        on_court_players = []
        weight_probability = []
        sum_total_off_part = 0
        for player_name in self.roster.keys():
            if (self.roster[player_name].on_court == True):
                   on_court_players.append(self.roster[player_name])
                   sum_total_off_part += self.roster[player_name].offense_participation  #aprovechamos el bucle para sumar esta variable
        
        for player in on_court_players:
            weight_probability.append(float(player.offense_participation / sum_total_off_part))

        return choice(on_court_players, 1, p=weight_probability)[0]   #de este modo solo nos devuelve un elemento y no un array

    
    def select_random_on_court_player(self):
        on_court_players = []
        for player_name in self.roster.keys():
            if (self.roster[player_name].on_court == True):
                   on_court_players.append(self.roster[player_name])
        
        return random.choice(on_court_players).name
        
        
    def select_random_assistant_player(self, scoring_player_name):
        on_court_poss_assistant_players = []
        for player_name in self.roster.keys():
            if (self.roster[player_name].on_court == True) and (player_name != scoring_player_name):
                   on_court_poss_assistant_players.append(self.roster[player_name])
        
        return random.choice(on_court_poss_assistant_players).name
    
    def get_total_team_points(self):
        total_points = 0

        for player_name in self.roster.keys():
            total_points += self.roster[player_name].get_points_made()
        
        return total_points

        


        



