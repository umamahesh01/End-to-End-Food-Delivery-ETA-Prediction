import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Encoding:

    def __init__(self):
        
        self.encoded = {}      # store encoders for each column

    def encode(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:

        df = df.copy()

        for i in cols:
            le = LabelEncoder()
            df[i] = le.fit_transform(df[i])

            self.encoded[i] = le       # store this column's encoder

        return df
    
    def transform(self, df: pd.DataFrame) :

        df = df.copy()

        for col,le in self.encoded.items():    # here le is label encoder stored in self.encoded 
            df[col] = le.transform(df[col])

        return df 