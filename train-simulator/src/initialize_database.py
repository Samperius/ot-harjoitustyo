from src.database_connection import get_database_connection
import os
import pandas as pd
def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists track;
    ''')
    cursor.execute('''
        drop table if exists stop_coordinates;
    ''')
    cursor.execute('''
        drop table if exists bottlenecks;
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
    track = pd.read_csv(pathtocsv)  # load to DataFrame
    track.to_sql('track', connection, if_exists='append', index=False)  # write to sqlite table
    #stop coordinates:
    cursor.execute('''
        create table stop_coordinates (
            stop text primary key,
            y integer,
            x integer
        );
    ''')
    pathtocsv = os.path.join(dirname, "data", "stop_coordinates.csv")
    stop_coordinates = pd.read_csv(pathtocsv)  # load to DataFrame
    stop_coordinates.to_sql('stop_coordinates', connection, if_exists='append', index=False)  # write to sqlite table
    #bottleneck:
    cursor.execute('''
        create table bottlenecks (
            bottleneck text primary key,
            capacity integer,
            y integer,
            x integer
        );
    ''')
    pathtocsv = os.path.join(dirname, "data", "bottlenecks.csv")
    bottlenecks = pd.read_csv(pathtocsv)  # load to DataFrame
    bottlenecks.to_sql('bottlenecks', connection, if_exists='append', index=False)  # write to sqlite table
def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
