import pandas as pd
from sklearn.linear_model import LinearRegression
import os
import pickle

class Model:

    def __init__(self):
        self.model = LinearRegression()

    def train(self, x,y):
        self.model.fit(x,y)


    def save(self,path :str):
        os.makedirs(os.path.dirname(path), exist_ok=True)   # creates artifacts folder
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)


        