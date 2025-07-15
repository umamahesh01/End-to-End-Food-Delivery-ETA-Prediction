import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yaml
from src.data.data_loader import Loader


with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# data loading
loading = Loader(config['data_path'])
df = loading.load()

sns.boxplot(df['cost_of_the_order'])
plt.show()

sns.boxplot(df['delivery_time'])
plt.show()
