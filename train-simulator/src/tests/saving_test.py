import unittest
from repositories.saving import Saving
import pandas as pd
from config import RESULTS_PATH

class TestTrackRepo(unittest.TestCase):
    def setUp(self):
        data = {'number_of_simulations': [1],
                'number_of_trains': [4],
                'average_waiting_time': [5.6]}
        self.saving = Saving()
        self.saving.save_dataframe(data)

    def test_saving_simulations(self):
        df = pd.read_csv(RESULTS_PATH)
        simulations = df.iloc[-1,0]
        self.assertEqual(simulations, 1)

    def test_trains_trains(self):
        df = pd.read_csv(RESULTS_PATH)
        trains = df.iloc[-1,1]
        self.assertEqual(trains, 4)

    def test_saving_waiting(self):
        df = pd.read_csv(RESULTS_PATH)
        waiting = df.iloc[-1,2]
        self.assertEqual(waiting, 5.6)

