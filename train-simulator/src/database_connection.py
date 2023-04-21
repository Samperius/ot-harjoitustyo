import os
import sqlite3

dirname = os.path.dirname("/home/samuli/School/OT/ot-harjoitustyo/train-simulator/")
pathtodatabase = os.path.join(dirname, "data","TrainSimulator.db")
connection = sqlite3.connect(pathtodatabase)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection


"""def main():
    connection = get_database_connection()

main()"""