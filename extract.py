import pandas as pd


def read_helsinki_file(path, delimeter):
    df = pd.read_csv(path, delimiter=delimeter)
    df["Emotions"] = df["Emotions"].apply(lambda x: [int(emotion_id)
                                                     for emotion_id in x.split(",")
                                                     if emotion_id.strip().isdigit()])
    return df


def use_data():
    df = read_helsinki_file("data/csv_translated.csv", "\t")
    print(df.head())


use_data()
