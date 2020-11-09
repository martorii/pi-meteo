import mysql.connector
import pandas as pd

host = 'localhost'
database='METEO'
user='pi'
password='raspberrymeteo'

def Select(query):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(data, columns = columns)
        
        connection.commit()
        return data
    
    except mysql.connector.Error as error:
        print(error)
        return None

def Insert(query):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as error:
        print(error)
    return