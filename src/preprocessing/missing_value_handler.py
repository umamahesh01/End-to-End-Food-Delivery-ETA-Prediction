import pandas as pd

class Handling:

    def __init__(self,num_method = None, cat_method = None, fill_value = None):
        self.num_method = num_method
        self.cat_method = cat_method
        self.fill_value = fill_value
    
    def handle(self, df: pd.DataFrame):
        df = df.copy()

        for i in df.select_dtypes(include= 'object'):
            
            if self.cat_method == 'median':
                df[i] = df[i].fillna(df[i].median())
            elif self.cat_method == 'mode':
                df[i] = df[i].fillna(df[i].mode()[0])
            elif self.cat_method == 'constant':
                df[i] = df[i].fillna(self.fill_value)
            else:
                raise ValueError("Invalid method. Use 'median', 'mode', or 'constant'.")

        
        for i in df.select_dtypes(exclude= 'object'):
            
            if self.num_method == 'mean':
                df[i] = df[i].fillna(round(df[i].mean(),1))
            elif self.num_method == 'median':
                df[i] = df[i].fillna(df[i].median())
            elif self.num_method == 'mode':
                df[i] = df[i].fillna(df[i].mode()[0])
            elif self.num_method == 'constant':
                df[i] = df[i].fillna(self.fill_value)
            else:
                raise ValueError("Invalid method. Use 'mean', 'median', 'mode', or 'constant'.")

    
        return df



    