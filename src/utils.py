import os 
import sys

import dill
import pandas as pd
import numpy as np

from src.exception import CustomException
from sklearn.metrics import r2_score
 
def save_object(file_path: str, obj: object) -> None:
    '''
    This function is used to save the object to a file using dill
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
def evaluate_models(X_train, y_train, X_test, y_test, models):
    '''
    This function evaluates multiple machine learning models and returns their R2 scores.
    '''
    try:
        report = {}

        for model_name, model in models.items():
            # Train the model
            model.fit(X_train, y_train)

            # Make predictions
            y_test_pred = model.predict(X_test)

            # Calculate R2 score
            r2_square = r2_score(y_test, y_test_pred)

            report[model_name] = r2_square

        return report

    except Exception as e:
        raise CustomException(e, sys)
