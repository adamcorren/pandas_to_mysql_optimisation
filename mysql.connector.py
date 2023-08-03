import pandas as pd
import mysql.connector
from datetime import datetime
import sample_df
import time


def get_data():
    data = sample_df.create_test_df(1000000)
    return data


def connect_server():
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'aj_198aj_198',
        'database': 'git'
    }
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    return cursor, connection


def insert(df, cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS data (
        string VARCHAR(10),
        int_num INT,
        float_num DECIMAL (4, 2),
        bool_int INT,
        dates DATE
    )
    """
    cursor.execute(create_table_query)

    for index, row in df.iterrows():
        row = row.where(pd.notna(row), None)
        insert_race_data_query = "INSERT INTO data (string, int_num, float_num, bool_int, dates) " \
                                 "VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(insert_race_data_query, (row['string'], row['integer_num'], row['float_num'], row['boolean'], row['dates']))


def main():
    df = get_data()
    sizes = [100, 1000, 10000, 100000, 250000, 500000, 1000000]
    for s in sizes:
        start_time = time.time()
        df = df.sample(s, replace=True)
        cursor, connection = connect_server()
        insert(df, cursor)
        connection.commit()
        connection.close()
        end_time = time.time()
        runtime = end_time - start_time
        print(f"{s} rows runtime: {runtime:.5f} seconds")


main()