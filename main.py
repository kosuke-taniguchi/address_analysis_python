from locale import getpreferredencoding
from unittest import result
import pandas as pd

def get_prefecture_and_city():
    pref_and_city_csv_data = pd.read_csv("./KEN_ALL_ROME.csv", usecols=[1])
    
    result = pref_and_city_csv_data.drop_duplicates()
    for r in result.iterrows():
        splited = r[1].astype(str).split("GUN")
        print(splited)
    # result.to_csv("./results/results.csv")

def get_prefectures():
    csv_data = pd.read_csv("./KEN_ALL_ROME.csv", usecols=[0])

    result = csv_data.drop_duplicates(subset="KEN")
    result.to_csv("./results/prefectures.csv", index=False)


if __name__ == "__main__":
    get_prefecture_and_city()
    get_prefectures()