from player import Player
from team import Team

def players_team_loader():
    #Instantation of Players
    player_1_local = Player(ID_player= 1, name= "J. Jackson Jr.", position = "4", fga_1_average= 0.83, fga_2_average= 0.51, fga_3_average= 0.39, offense_participation= 3, on_court = True)
    player_2_local = Player(ID_player= 2, name= "D. Brooks", position = "3", fga_1_average= 0.85, fga_2_average= 0.45, fga_3_average= 0.40, offense_participation=2, on_court = True)
    player_3_local = Player(ID_player= 3, name= "S. Adams", position = "5", fga_1_average= 0.75, fga_2_average= 0.52, fga_3_average= 0.15, offense_participation = 1, on_court = True)
    player_4_local = Player(ID_player= 4, name= "J. Morant", position = "1", fga_1_average= 0.88, fga_2_average= 0.50, fga_3_average= 0.38, offense_participation = 3, on_court = True)
    player_5_local = Player(ID_player= 5, name= "D. Bane", position = "2", fga_1_average= 0.85, fga_2_average= 0.40, fga_3_average= 0.43, offense_participation = 3, on_court = True)
    
    player_6_local = Player(ID_player= 6, name= "T. Jones", position = "1", fga_1_average= 0.76, fga_2_average= 0.32, fga_3_average= 0.35, offense_participation = 1, on_court = False)
    player_7_local = Player(ID_player= 7, name= "Z. Williams", position = "2",fga_1_average= 0.89, fga_2_average= 0.42, fga_3_average= 0.38, offense_participation = 2, on_court = False)
    player_8_local = Player(ID_player= 8, name= "K. Anderson", position = "3",fga_1_average= 0.90, fga_2_average= 0.40, fga_3_average= 0.39, offense_participation = 2, on_court = False)
    player_9_local = Player(ID_player= 9, name= "B. Clarke", position = "4",fga_1_average= 0.82, fga_2_average= 0.45, fga_3_average= 0.30, offense_participation = 2, on_court = False)
    player_10_local = Player(ID_player= 10, name= "X. Tillman", position = "5",fga_1_average= 0.70, fga_2_average= 0.43, fga_3_average= 0.25, offense_participation = 1, on_court = False)
    local_players_ls = [player_1_local, player_2_local, player_3_local, player_4_local, player_5_local, player_6_local, player_7_local, player_8_local, player_9_local, player_10_local]

    player_1_abroad = Player(ID_player= 11, name= "J. Vanderbilt", position = "4", fga_1_average= 0.75, fga_2_average= 0.38, fga_3_average= 0.37, offense_participation= 1, on_court = True)
    player_2_abroad = Player(ID_player= 12, name= "A. Edwards", position = "3", fga_1_average= 0.84, fga_2_average= 0.48, fga_3_average= 0.36, offense_participation=3, on_court = True)
    player_3_abroad = Player(ID_player= 13, name= "K. Towns", position = "5", fga_1_average= 0.90, fga_2_average= 0.55, fga_3_average= 0.42, offense_participation = 3, on_court = True)
    player_4_abroad = Player(ID_player= 14, name= "P. Beverly", position = "2", fga_1_average= 0.81, fga_2_average= 0.41, fga_3_average= 0.35, offense_participation = 2, on_court = True)
    player_5_abroad = Player(ID_player= 15, name= "D. Russell", position = "1", fga_1_average= 0.89, fga_2_average= 0.46, fga_3_average= 0.39, offense_participation = 3, on_court = True)
    
    player_6_abroad = Player(ID_player= 6, name= "J. McLaughlin", position = "1", fga_1_average= 0.79, fga_2_average= 0.33, fga_3_average= 0.30, offense_participation = 1, on_court = False)
    player_7_abroad = Player(ID_player= 7, name= "M. Beasley", position = "2",fga_1_average= 0.88, fga_2_average= 0.36, fga_3_average= 0.41, offense_participation = 2, on_court = False)
    player_8_abroad = Player(ID_player= 8, name= "J. McDaniels", position = "3",fga_1_average= 0.88, fga_2_average= 0.35, fga_3_average= 0.40, offense_participation = 2, on_court = False)
    player_9_abroad = Player(ID_player= 9, name= "T. Prince", position = "4",fga_1_average= 0.76, fga_2_average= 0.39, fga_3_average= 0.30, offense_participation = 1, on_court = False)
    player_10_abroad = Player(ID_player= 10, name= "N. Reid", position = "5",fga_1_average= 0.72, fga_2_average= 0.42, fga_3_average= 0.28, offense_participation = 1, on_court = False)
    abroad_players_ls = [player_1_abroad, player_2_abroad, player_3_abroad, player_4_abroad, player_5_abroad, player_6_abroad, player_7_abroad, player_8_abroad, player_9_abroad, player_10_abroad]

    #We generate the teams
    local_Team = Team(team_name = "Memphis Grizzlies", is_local_team = True, team_conference = "West")
    abroad_Team = Team(team_name = "Minnesota Timberwolves", is_local_team = False, team_conference = "West")

    #we populate the Teams with its players
    for player in local_players_ls:
        local_Team.add_player_to_roster(player)
    
    for player in abroad_players_ls:
        abroad_Team.add_player_to_roster(player)
    
    #we return the Teams with its players in it
    return local_Team, abroad_Team
