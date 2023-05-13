import pandas as pd
import os
from config import RESULTS_PATH


class Saving:
    def __init__(self, result_path = RESULTS_PATH):
        self.file_path = result_path
        self.file_exists = os.path.isfile(result_path)

    def save_dataframe(self, data):
        df = pd.DataFrame(data)
        if self.file_exists:
            df.to_csv(self.file_path, mode='a', index=False, header=False)
        else:
            df.to_csv(self.file_path, mode='w', index=False, header=True)
