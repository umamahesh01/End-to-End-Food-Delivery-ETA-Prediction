from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

class Evaluation:

    def eval(y_true, y_pred):
        mae = mean_absolute_error(y_true, y_pred)
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_true, y_pred)

        print('mae',mae)
        print('mse',mse)
        print('rmse', rmse)
        print('r2', r2)
