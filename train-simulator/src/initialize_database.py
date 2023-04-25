import pandas as pd
from database_connection import get_database_connection
from config import TRACK_INFO_PATH, STOP_COORDINATE_PATH, BOTTLENECKS_PATH


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
    #track:
    cursor.execute('''
        create table track (
            start text primary key,
            dest text,
            distance integer,
            speedlimit integer
        );
    ''')
    track = pd.read_csv(TRACK_INFO_PATH)  # load to DataFrame
    track.to_sql('track', connection, if_exists='append', index=False)  # write to sqlite table
    #stop coordinates:
    cursor.execute('''
        create table stop_coordinates (
            stop text primary key,
            y integer,
            x integer
        );
    ''')
    stop_coordinates = pd.read_csv(STOP_COORDINATE_PATH)
    stop_coordinates.to_sql('stop_coordinates', connection, if_exists='append', index=False)
    #bottleneck:
    cursor.execute('''
        create table bottlenecks (
            bottleneck text primary key,
            capacity integer,
            y integer,
            x integer
        );
    ''')
    bottlenecks = pd.read_csv(BOTTLENECKS_PATH)
    bottlenecks.to_sql('bottlenecks', connection, if_exists='append', index=False)
def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
