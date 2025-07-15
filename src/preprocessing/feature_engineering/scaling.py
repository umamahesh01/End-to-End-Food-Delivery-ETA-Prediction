import pandas as pd
from sklearn.preprocessing import StandardScaler

class ScalingWapper:

    def __init__(self):
        self.ss = StandardScaler()

    def scaling(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:
        
        df = df.copy()

        df[cols] = self.ss.fit_transform(df[cols])

        return df
    
    def transform(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:

        df = df.copy()

        df[cols] = self.ss.transform(df[cols])

        return df



