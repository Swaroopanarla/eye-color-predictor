import pandas as pd
from model import EyeModel

def main():
    data = pd.read_csv("eye_dataset.csv")

    print("👁️ Eye Color Prediction System")
    eye = input("Enter eye color: ").lower()

    result = data[data["eye_color"].str.lower() == eye]

    if result.empty:
        print("❌ No data found")
    else:
        print("\n📊 Countries with this eye color:\n")
        print(result)

    model = EyeModel(data)
    model.train()

    try:
        prediction = model.predict(eye)
        print("\n🌍 Predicted Country:", prediction)
    except:
        print("⚠️ Eye color not in model")

if __name__ == "__main__":
    main()