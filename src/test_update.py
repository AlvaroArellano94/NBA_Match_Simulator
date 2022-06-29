from Insert_Module import insert_values_into_DB
import time
from player import Player
from team import Team
import pypyodbc as odbc
from pyodbc_NBA import connect_to_db
import pandas as pd 
import sys
import datetime

winner_Team_Id = 1
match_id=9

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
    date_time = datetime.datetime.now()
    print(type(date_time))
    # convert timestamp to string in dd-mm-yyyy HH:MM:SS
    print(date_time)
    str_date_time = date_time.strftime('%Y%m%d %H:%M:%S')
    #str_date_time = date_time.strftime("%Y%m%d %H:%M:%S")
    #str_date_time = "20220629 14:12:09"
    print(str_date_time)
    print(type(str_date_time))
    new_test = "20220629 14:39:00"
    #new_str = str_date_time[:-2]+'00'
    ######select_str_Match = f'UPDATE dbo.Match SET Start_Time={new_test}, Winner_Team_Id={winner_Team_Id} where Id_Match={match_id};'
    
    select_str_Match = f'UPDATE dbo.Match SET Start_Time=?, Winner_Team_Id=? where Id_Match=?;'
    #select_str_Match = f'UPDATE dbo.Match SET Winner_Team_Id={winner_Team_Id}, End_Time={str_date_time} where Id_Match={match_id};'
    ls_to_insert = [str_date_time, 1, 9]
    print(select_str_Match)
    cursor.execute(select_str_Match, ls_to_insert)

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