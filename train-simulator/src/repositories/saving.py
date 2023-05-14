import os
import pandas as pd
from config import RESULTS_PATH


class Saving:
    """
    tallennusluokka

    Attributes:
        file_path: merkkijono tai os.path-muuttuja joka osoittaa tiedoston sijainnin
    """
    def __init__(self, result_path = RESULTS_PATH):
        """
        Luokan konstruktori
        :param result_path: merkkijono tai os.path-muuttuja joka osoittaa tiedoston sijainnin
        """
        self.file_path = result_path


    def save_dataframe(self, data):
        """
        metodi, joka ottaa datan ja tallentaa sen csv-muodossa
        :param data: dict-tietue, joka sisältää tallennettavan datan
        """
        file_exists = os.path.isfile(self.file_path)
        data_frame = pd.DataFrame(data)
        if file_exists:
            data_frame.to_csv(self.file_path, mode='a', index=False, header=False)
        else:
            data_frame.to_csv(self.file_path, mode='w', index=False, header=True)
