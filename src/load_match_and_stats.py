from Insert_Module import insert_values_into_DB
import time
from player import Player
from team import Team
import pypyodbc as odbc
from pyodbc_NBA import connect_to_db
import pandas as pd 
import sys
import datetime

##Primero vamos a insertar la info sobre el match

####IT NEEDS TO BE TESTED!!!
def insert_match_to_db(local_Team, abroad_Team):
    #insert_table, fields_to_insert, records_to_insert
    #remember that Id_Match is created by the database
    date_time = datetime.now()
    # convert timestamp to string in dd-mm-yyyy HH:MM:SS
    str_date_time = date_time.strftime("%Y%m%d %H:%M:%S")

    fields_to_insert = ['Id_Team_Local', 'Id_Team_Abroad', 'Start_Time', 'End_Time', 'Winner_Team_Id']
    records_to_insert = [local_Team.ID_Team, abroad_Team.ID_Team, str_date_time, None, None]
    insert_values_into_DB('Match', fields_to_insert, records_to_insert)

def update_match_info_to_db(match_id, winner_Team_Id):
    #debemos realizar un update actualizando los campos: "End_Time" y "Winner_Team_Id" ahora que ya tenemos esa información
    try:
        print('test')
        connection = connect_to_db()
    except Exception as e:
        print(e)
        print("Task is not being completed.")
    else:
        cursor = connection.cursor()
    
    try:
        #Vamos a realizar
        date_time = datetime.now()
        # convert timestamp to string in dd-mm-yyyy HH:MM:SS
        str_date_time = date_time.strftime("%Y%m%d %H:%M:%S")

        select_str_Match = f'UPDATE dbo.Match SET End_Time={str_date_time}, Winner_Team_Id={winner_Team_Id} where Id_Match={match_id};'
        print(select_str_Match)
        max_id_cursor = cursor.execute(select_str_Match)

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

def get_match_id(local_Team, abroad_Team):
    #hago un select con todos los registros que tienen estos dos equipos y me quedo con el que tenga "str_date_time", que será el más actual...
    #posteriormente, voy a hacer return de solo el id_match
    #primero generamos una conexión con la bbdds
    try:
        print('test')
        connection = connect_to_db()
    except Exception as e:
        print(e)
        print("Task is not being completed.")
    else:
        cursor = connection.cursor()
    
    try:
        #Vamos a realizar
        select_str_Match = f'SELECT max(Id_Match) FROM dbo.Match where Id_Team_Local={local_Team} and Id_Team_Abroad={abroad_Team};'
        print(select_str_Match)
        max_id_cursor = cursor.execute(select_str_Match)
        for max_id_Match in max_id_cursor:
            id_Match = max_id_Match

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
    
    return id_Match


#Insertamos la info sobre Player_Stats_Match
def insert_player_stats_Match_to_db(id_Match, player_obj, id_Team):
    #It needs to be iterated
    #it needs Id_Match -> ¿it needs match to be passed? -> we have created before, so it is not difficult... the object or the id itself? The object
    #it needs Id_player (from both teams)
    #Id_Team -> from teams can be extracted
    fields_to_insert = ['Id_Match', 'Id_Player', 'Id_Team', 'Attempt_1', 'Attempt_1_Made', 'Attempt_2', 'Attempt_2_Made', 'Attempt_3', 'Attempt_3_Made',\
         'Points_Made', 'Assists_Made', 'Steals_Made', 'Blocks_Made', 'Turnovers_Made', 'Fouls_Made', 'Fouled_Out', 'On_Court', 'Seconds_Played']
    #TODO: add the rest of the fields
    player_fouled_out_bit = 1 if player_obj.fouled_out == True else 0
    player_on_court_bit = 1 if player_obj.on_court == True else 0
    records_to_insert = [id_Match, player_obj.ID_player, id_Team, player_obj.attempts_statistics['attempt_1'], player_obj.attempts_statistics['attempt_1_Made'],\
        player_obj.attempts_statistics['attempt_2'], player_obj.attempts_statistics['attempt_2_Made'],player_obj.attempts_statistics['attempt_3'],\
        player_obj.attempts_statistics['attempt_3_Made'], player_obj.get_points_made(), player_obj.assists_num, player_obj.steals_num, player_obj.blocks_num, \
        player_obj.turnovers_num, player_obj.fouls_num, player_fouled_out_bit, player_on_court_bit, player_obj.seconds_played]
        
    insert_values_into_DB("Player_Stats_Match", fields_to_insert, records_to_insert)

