from src.database_connection import get_database_connection
import os
import pandas as pd
def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists track;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table track (
            start text primary key,
            dest text,
            distance integer,
            speedlimit integer
        );
    ''')

    dirname = os.path.dirname("/home/samuli/School/OT/ot-harjoitustyo/train-simulator/")
    pathtocsv = os.path.join(dirname, "data", "track.csv")
    orders = pd.read_csv(pathtocsv)  # load to DataFrame
    #print(orders.columns)
    orders.to_sql('track', connection, if_exists='append', index=False)  # write to sqlite table

    row1 = cursor.execute(f"select dest from track where start='Helsinki-P'")
    row1 = row1.fetchone()
    print(row1[0])
    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
