import pandas as pd

class Dropper:

    def __init__(self):
        self.dropped_cols = []

    def drop(self, df: pd.DataFrame, cols : list):
        df = df.copy()

        df.drop(columns = cols, inplace= True)
        self.dropped_cols.extend(cols)

        return df
