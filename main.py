from operator import index
import pandas as pd


def get_city_csv_data():
    """get_city_csv_data
    日本の市（特別区を含む）データを取得する
    また、MySQLへInsertする際に必要な外部キーも順番に貼っていく
    """
    pref_and_city_csv_data = pd.read_csv("./ken_shi.csv")

    new_df = pd.DataFrame(columns=["prefecture_id", "name"])
    temp_idx = 0
    temp_pref = ""
    for i, pref in enumerate(pref_and_city_csv_data.iterrows()):
        print(i)
        if temp_pref != pref[1]["KEN"]:  
            temp_idx += 1
            temp_pref = pref[1]["KEN"]

        child_df = pd.DataFrame({"prefecture_id": temp_idx, "name": pref[1]["SHI"]}, index=[0])
        new_df = pd.concat([new_df, child_df])
    
    new_df.to_csv("./results/city.csv")


def add_country_to_pref_and_city_data():
    pref_and_city_csv_data = pd.read_csv("./ken_shi.csv")
    pref_and_city_csv_data.insert(loc=0, column="country", value="日本")
    pref_and_city_csv_data.to_csv("./results/country_pref_city.csv", index=False)


if __name__ == "__main__":
    # get_city_csv_data()
    add_country_to_pref_and_city_data()