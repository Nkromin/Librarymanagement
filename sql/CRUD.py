import pandas as pd

import os

CSV_FILE = "books.csv"
COLUMNS =["id", "title", "author", "genre", "year", "available"]

def load_data():
    if not os.path.exists(CSV_FILE):
        pd.DataFrame(columns=COLUMNS).to_csv(CSV_FILE, index=False)

    return pd.read_csv(CSV_FILE)





def save_data(df: pd.DataFrame):
    df.to_csv(CSV_FILE, index=False)




def next_id(df):
   return 1 if df.empty else df["id"].max() + 1