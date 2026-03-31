import pandas as pd

def load_data():
    data = pd.read_csv("eye_dataset.csv")
    return data

def get_info_by_eye_color(data, eye_color):
    result = data[data["eye_color"].str.lower() == eye_color.lower()]
    return result