import pandas as pd
import numpy as np
import yaml
import seaborn as sns 
import matplotlib.pyplot as plt
from src.data.data_loader import Loader
from src.preprocessing.missing_value_handler import Handling
from src.preprocessing.feature_dropper import Dropper
from src.preprocessing.feature_engineering.endcoder import Encoding
from src.preprocessing.feature_engineering.scaling import ScalingWapper
from src.model.model_eval import Evaluation
from src.model.model_train import Model
from sklearn.model_selection import train_test_split
from src.preprocessing.feature_engineering.outlier_removal import Remove_Outliers



with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)


# Loading Data
loading = Loader(config['data_path'])
df = loading.load()


# Dropping unncessary columns
dropping = Dropper()
df = dropping.drop(df, cols = ['order_id','customer_id','rating'])


# Dropping Outliers
df = Remove_Outliers(df, 'cost_of_the_order')

# Handling Missing Values
mod = Handling(num_method = 'mean',cat_method = 'mode') 
df = mod.handle(df)

# Encoding
new_cols = df.drop(columns=[config['target_columns']]).columns
end = Encoding()
df = end.encode(df, new_cols)


# Scaling
scale = ScalingWapper()
df = scale.scaling(df, new_cols)

# X,y
X = df.drop(columns = config['target_columns'])
y = df[config['target_columns']]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2 ,random_state=42)

# Training
trainer = Model()
trainer.train(X_train,y_train)
trainer.save(config['model_path'])

# Evaluation
y_pred = trainer.model1.predict(X_test)
score = Evaluation.eval(y_test, y_pred)



