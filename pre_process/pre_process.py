import pandas as pd


def pre_process():
    dfs = []
    csv_files = ['EUmatch.csv', 'KRmatch.csv', 'NAmatch.csv']
    for file_name in csv_files:
        df_temp = pd.read_csv(file_name)
        dfs.append(df_temp)

    merged = pd.concat(dfs)

    merged = merged.drop(columns=['d_spell', 'f_spell', 'side', 'time_cc', 'level', 'kills', 'deaths', 'damage_taken', 'assists'])
    merged = merged.dropna()
    merged.to_csv("merged.csv", index=False)
