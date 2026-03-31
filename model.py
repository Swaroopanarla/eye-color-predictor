import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

class EyeModel:
    def __init__(self, data):
        self.data = data
        self.le = LabelEncoder()
        self.model = DecisionTreeClassifier()

    def train(self):
        self.data['eye_color_encoded'] = self.le.fit_transform(self.data['eye_color'])
        X = self.data[['eye_color_encoded']]
        y = self.data['country']
        self.model.fit(X, y)

    def predict(self, eye_color):
        encoded = self.le.transform([eye_color])[0]
        return self.model.predict([[encoded]])[0]