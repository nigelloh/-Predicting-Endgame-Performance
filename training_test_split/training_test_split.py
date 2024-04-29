import pandas as pd
from sklearn.model_selection import train_test_split


def evaluation():
    df = pd.read_csv('merged.csv')
    train, test = train_test_split(df, test_size=0.3)
    test.to_csv("testing.csv", index=False)
    train.to_csv("training.csv", index=False)

