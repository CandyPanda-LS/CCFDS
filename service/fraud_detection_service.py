import joblib
import xgboost as xgb


class FraudDetectionService:
    def __init__(self):
        self.model = joblib.load('model/xgb_classifier_model.pkl')

    def is_fraud(self):
        print("test")
        return {"is_fraud": self.model.predict([[2.13195566599056, 56.3724005365082, 6.35866732163061, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0]])}

