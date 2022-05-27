from player import Player  #hola
from team import Team
from load_teams import players_team_loader
from match import play_possession_by_quarter, action_by_possesion, rebound_result, rebound_action, type_shoot_weight_selection, change_possession_rebound
import random
#¿Inicializar el seed?
import time
from numpy.random import choice
import sys

if __name__ == "__main__":
    
    #This function loads the players and assign them to its teams. It returns two teams.
    local_Team, abroad_Team = players_team_loader()
    
    #here you can find each 
    quarter_time_dict = {
        1: 720,
        2: 1440,
        3: 2160,
        4: 2880
    }

    #Here I am creating the variables and inform them as the beginning of the match
    game_t_count = 0 #variable that counts the seconds of the game
    possession_Item = round(random.random()) #0 (will be local_Team) or 1(will be abroad_Team). 
    team_ls = [local_Team, abroad_Team]
    quarter_num = 1  #in the last possession of the quarter, this value will be incremented in 1. 

    #now the match starts, 
    while game_t_count <= quarter_time_dict[4]:
        #first, check if it's the last possession
        last_possession_quarter = False if game_t_count < (quarter_time_dict[quarter_num] - 24) else True
        #seconds of current possession. If less than 24 seconds, the value is the rest until that time
        possession_time = random.randint(1, 24) if not last_possession_quarter else (quarter_time_dict[quarter_num] - game_t_count)
        #the time of the possession is played, the time its updated and it's being returned.  
        game_t_count = play_possession_by_quarter(game_t_count, quarter_time_dict[quarter_num], possession_time)

        #update seconds played by every player (it need to be done every possession):
        abroad_Team.update_seconds_played(possession_time)
        local_Team.update_seconds_played(possession_time)

        #vamos a realizar la jugada en si:
        action = action_by_possesion() #it returns a string with the action of this possession

        #¿which team is attacking?
        possession_team = team_ls[possession_Item]  #it tells what team is attacking
        defending_team = team_ls[1 if possession_Item == 0 else 0] 
        print(f"{possession_team.team_name} is the team with the possession (attacking). {defending_team.team_name} is defending.")
        #at the end, we need to change possession_Item, if there are not an offensive rebound or 
        player_attacking = possession_team.attack_player()
        print(f"{player_attacking.name} has the ball and is attacking.")

        if action == "field_attempt":
            type_shoot =  type_shoot_weight_selection()#it returns an array of one element. For this reason, we take only the first element
            result_attempt = player_attacking.field_goal_attempt(type_shoot)
            player_attacking.update_field_goal_attempt(type_shoot, result_attempt)

            is_assist_perc = random.random()
            if result_attempt==False:
                print(f"The {player_attacking.name} has attempted a basket of {type_shoot} and has failed.")
            if is_assist_perc >= 0.65 and result_attempt==True:
                #message     
                print(f"The {player_attacking.name} has attempted a basket of {type_shoot} and has successed.")

            elif is_assist_perc < 0.65 and result_attempt==True:
                name_assist_player = possession_team.select_random_assistant_player(player_attacking.name)  #we passed the name of the player that scores  
                possession_team.roster[name_assist_player].assist_made()
                #message
                print(f"The {player_attacking.name} has attempted a basket of {type_shoot}, has successed and {name_assist_player} has made an assist.")
            
            #the shot has been made so possession needs to change 
            if result_attempt == True:
                possession_Item = 1 if possession_Item == 0 else 0 #change possession

            #if it is a missed shoot, there will be a rebound. Depending on who catches the rebound, there will be or not a change on possession
            elif result_attempt == False:
                rebound_situation = rebound_result()  #it stores if it has been defensive or offensive rebound - will be used to change or not possession
                rebound_action(rebound_situation, defending_team, possession_team)  #used to update statistics, depending on if it has been defensive or offensive rebound

                #the print message is into the "rebound action function"
                possession_Item = change_possession_rebound(rebound_situation, possession_Item)

                               

        #action="only_turnover"
        elif action == "only_turnover":
            player_attacking.turnover_made()
            #message
            print(f"{player_attacking.name} has made a turnover.")
            possession_Item = 1 if possession_Item == 0 else 0 #change possession
        
        #action="turnover_+_steal"
        elif action == "turnover_+_steal":
            player_attacking.turnover_made()
            name_steal_player = defending_team.select_random_on_court_player()
            defending_team.roster[name_steal_player].steal_made()

            print(f"{player_attacking.name} has made a turnover and {name_steal_player} has stealed the ball.")
            possession_Item = 1 if possession_Item == 0 else 0 #change possession

        #fouls situation are a little bit special so it is treated separately
        foul_action_ls = ["throw_in", "two_FT", "two_+_1_FT", "three_+_1_FT"]

        if action in foul_action_ls:
            #we are going to select randomly who did the foul and make the statistic
            foul_committing_player = defending_team.roster[defending_team.select_random_on_court_player()]
            foul_committing_player.foul_made()
            #message
            print(f"{foul_committing_player.name} has made a foul.")
            #in case is being fouled out, it needs to be change_out
            if foul_committing_player.fouled_out == True:
                #message
                print(f"{foul_committing_player.name} has made a foul and has been fouled out.")
                #there is the obligation to change the player.
                defending_team.change_on_court_player(foul_committing_player)
                
        #we start another "if" with the same variable
        if action == "throw_in":
            #message
            print(f"{possession_team.team_name} has the ball for a throw_in.")
            pass
            #in this case, the fouled has been already counted, so the posetion goes on keeping the ball the same team
            #there is not a change in possession.

        ##action="two_FT"
        elif action == "two_FT":
            #first, free throw
            first_FT_result = player_attacking.field_goal_attempt(1)
            player_attacking.update_field_goal_attempt(1,first_FT_result)
            #message
            print(f"{player_attacking} has two free throws.")
            print(f"{player_attacking} has scored the first free throw.") if first_FT_result == True else print(f"{player_attacking} has failed the first free throw.")

            second_FT_result = player_attacking.field_goal_attempt(1)
            player_attacking.update_field_goal_attempt(1,second_FT_result)
            #message
            print(f"{player_attacking} has scored the second free throw.") if second_FT_result == True else print(f"{player_attacking} has failed the second free throw.")


            #change in possession
            if second_FT_result == True:
                possession_Item = 1 if possession_Item == 0 else 0 #change possession

            elif second_FT_result == False:
                rebound_situation = rebound_result()
                rebound_action(rebound_situation, defending_team, possession_team)
                #the print message is into the "rebound action function"

                possession_Item = change_possession_rebound(rebound_situation, possession_Item)        

        ##action="two_+_1_FT"
        elif action == "two_+_1_FT":
            player_attacking.update_field_goal_attempt(2, True)
            #message
            print(f"{player_attacking} has scored a 2 point basket and has been fouled, so has 1 free throw.")
            


            is_assist_perc = random.random()
            if is_assist_perc < 0.65: #we already know it is a successful 2 points basket, so we delete it from the condition
                name_assist_player = possession_team.select_random_assistant_player(player_attacking.name)
                possession_team.roster[name_assist_player].assist_made()
                #message
                print(f"{name_assist_player} has made an assist.")
            
            first_FT_result = player_attacking.field_goal_attempt(1)
            player_attacking.update_field_goal_attempt(1,first_FT_result)
            
            #message
            print(f"{player_attacking} has scored the free throw.") if first_FT_result == True else print(f"{player_attacking} has failed the free throw.")

            if first_FT_result == True:
                possession_Item = 1 if possession_Item == 0 else 0 #change possession

            elif first_FT_result == False:
                rebound_situation = rebound_result()
                rebound_action(rebound_situation, defending_team, possession_team) #the print message is into the "rebound action function"

                #Depending on the rebound it changes or not the possession
                possession_Item = change_possession_rebound(rebound_situation, possession_Item) 

        ##action="three_+_1_FT"                
        elif action == "three_+_1_FT":
            player_attacking.update_field_goal_attempt(3, True)
            #message
            print(f"{player_attacking} has scored a 3 point basket and has been fouled, so has 1 free throw.")

            is_assist_perc = random.random()
            if is_assist_perc < 0.65: #we already know it is a successful 3 point basket, so we delete it from the condition
                name_assist_player = possession_team.select_random_assistant_player(player_attacking.name)
                possession_team.roster[name_assist_player].assist_made()

                #message
                print(f"{name_assist_player} has made an assist.")
            
            first_FT_result = player_attacking.field_goal_attempt(1)
            player_attacking.update_field_goal_attempt(1,first_FT_result)

            #message
            print(f"{player_attacking} has scored the free throw.") if first_FT_result == True else print(f"{player_attacking} has failed the free throw.")

            if first_FT_result == True:
                possession_Item = 1 if possession_Item == 0 else 0 #change possession
                
            elif first_FT_result == False:
                rebound_situation = rebound_result()
                rebound_action(rebound_situation, defending_team, possession_team) #the print message is into the "rebound action function"

                possession_Item = change_possession_rebound(rebound_situation, possession_Item) #depending on the result it changes or not the possession

        #Last possession logic
        if last_possession_quarter == True and quarter_num != 4:
            print(f"The {quarter_num} quarter has ended. The {quarter_num+1} quarter will start in 30 seconds.")

            quarter_num += 1
            time.sleep(30)

        elif last_possession_quarter == True and quarter_num == 4:
            print(f"The 4 quarter has ended.")
    
    #the end of the match
    
    print("The END")
