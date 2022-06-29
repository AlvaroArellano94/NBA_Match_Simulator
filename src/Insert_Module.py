import pypyodbc as odbc
from pyodbc_NBA import connect_to_db

def insert_values_into_DB(insert_table, fields_to_insert, records_to_insert):
    ins_str_1 = 'INSERT INTO '
    ins_table = insert_table+' ('
    ins_str_2 =''
    ins_str_3 =') VALUES ('
    ins_str_4 = ''

    counter = 0
    while counter < (len(fields_to_insert)-1): #we do that to avid the last 
        ins_str_2 += fields_to_insert[counter]+','
        ins_str_4 += '?,'
        counter += 1

    ins_str_2 += fields_to_insert[-1]
    ins_str_4 += '?);'

    insert_statement = ins_str_1+ins_table+ins_str_2+ins_str_3+ins_str_4

    try:
        connection = connect_to_db()
    except Exception as e:
        print(e)
        print("Task is not being completed.")
    else:
        cursor = connection.cursor()
    """
    try:
        for record in records_to_insert:
            #print(record)
            print(insert_statement)  #CHECKING
            print(record)
            cursor.execute(insert_statement, record) #we fill the interrogation marks of the first statement with thhe info into record 
    """
    try:
        print(insert_statement)        
        cursor.execute(insert_statement, records_to_insert)

    except Exception as e:
        cursor.rollback()  #to avoid inserting any
        print(e)
        print('transaction rolled back')
    else:
        print('records inserted successfully')
        cursor.commit()
    finally:           
        try:
            connection.close()
            print('connection closed')
        except Exception as e:
            print("The connection is already closed.")