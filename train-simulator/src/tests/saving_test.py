import unittest
import os
from repositories.saving import Saving
import pandas as pd
from config import dirname


RESULTS_FILENAME = "test_results.csv"
RESULTS_PATH = os.path.join(dirname, "..", "data", RESULTS_FILENAME)

class TestTrackRepo(unittest.TestCase):
    def setUp(self):
        self.data = {'number_of_simulations': [1],
                'number_of_trains': [4],
                'average_waiting_time': [5.6]}
        self.saving = Saving(RESULTS_PATH)
        self.saving.save_dataframe(self.data)
        self.df = pd.read_csv(RESULTS_PATH)
        os.remove(RESULTS_PATH)


    def test_saving_simulations(self):
        simulations = self.df.iloc[-1,0]
        self.assertEqual(simulations, 1)

    def test_trains_trains(self):
        trains = self.df.iloc[-1,1]
        self.assertEqual(trains, 4)

    def test_saving_waiting(self):
        waiting = self.df.iloc[-1,2]
        self.assertEqual(waiting, 5.6)

    def test_file_does_not_exist(self):
        self.saving.save_dataframe(self.data)
        self.df = pd.read_csv(RESULTS_PATH)
        waiting = self.df.iloc[-1, 2]
        self.assertEqual(waiting, 5.6)
        os.remove(RESULTS_PATH)



