import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "TrainSimulator.db"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

TRACk_INFO_FILENAME = os.getenv("TRACK_FILENAME") or "track.csv"
TRACK_INFO_PATH = os.path.join(dirname, "..", "data", TRACk_INFO_FILENAME)

STOPS_INFO_FILENAME = os.getenv("STOPS_FILENAME") or "stops.csv"
STOPS_INFO_PATH = os.path.join(dirname, "..", "data", STOPS_INFO_FILENAME)

STOP_COORDINATE_FILENAME = os.getenv("STOP_COORDINATE_FILENAME") or "stop_coordinates.csv"
STOP_COORDINATE_PATH = os.path.join(dirname, "..", "data", STOP_COORDINATE_FILENAME)

BOTTLENECKS_FILENAME = os.getenv("BOTTLENECKS_FILENAME") or "bottlenecks.csv"
BOTTLENECKS_PATH = os.path.join(dirname, "..", "data", BOTTLENECKS_FILENAME)
