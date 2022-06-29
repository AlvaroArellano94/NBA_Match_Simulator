from player import Player
from team import Team
import pypyodbc as odbc
from pyodbc_NBA import connect_to_db
import pandas as pd 
import sys

def players_team_loader():
    #Instantation of Players

    try:
        print('test')
        connection = connect_to_db()
        print('test')
    except Exception as e:
        print(e)
        print("Task is not being completed.")
    else:
        cursor = connection.cursor()

    try:
        #equipos creados!
        cursor_Memphis_info = cursor.execute('SELECT * FROM dbo.Teams where Id_Team=1')
        
        for team_info in cursor_Memphis_info:
            local_Team = Team(ID_Team= team_info[0], team_name = team_info[1], is_local_team = True, team_conference = team_info[2])

        cursor_Minessota_info = cursor.execute('SELECT * FROM dbo.Teams where Id_Team=2')
        for team_info in cursor_Minessota_info:
            abroad_Team = Team(ID_Team= team_info[0], team_name = team_info[1], is_local_team = False, team_conference = team_info[2])
        
        #Vamos a generar los jugadores
        select_str_Memphis = f'SELECT * FROM dbo.Players where Id_Player in (SELECT Id_Player FROM dbo.Rosters where Id_Team=1);'
        print(select_str_Memphis)
        cursor_Memphis_Players = cursor.execute(select_str_Memphis)

        for player in cursor_Memphis_Players:
            on_court_ls = True if player[0] in [1,2,3,4,5] else False
            player_i = Player(ID_player= player[0], name= player[1], position = player[2], fga_1_average= player[4], fga_2_average= player[5], fga_3_average= player[6], offense_participation=player[3], on_court = on_court_ls)
            local_Team.add_player_to_roster(player_i)

        select_str_Minessota = f'SELECT * FROM dbo.Players where Id_Player in (SELECT Id_Player FROM dbo.Rosters where Id_Team=2);'
        print(select_str_Minessota)
        cursor_Minessota_Players = cursor.execute(select_str_Minessota) 

        for player in cursor_Memphis_Players:
            on_court_ls = True if player[0] in [11,12,13,14,15] else False
            player_i = Player(ID_player= player[0], name= player[1], position = player[2], fga_1_average= player[4], fga_2_average= player[5], fga_3_average= player[6], offense_participation=player[3], on_court = on_court_ls)
            abroad_Team.add_player_to_roster(player_i) 

    except Exception as e:
        cursor.rollback()  #to avoid inserting any
        print(e)
        print('transaction rolled back')
    else:
        print('records read successfully')
        cursor.commit()
    finally:           
        try:
            connection.close()
            print('connection closed')
        except Exception as e:
            print("The connection is already closed.")
    
    #we return the Teams with its players in it
    return local_Team, abroad_Team