import pandas as pd

df = pd.read_csv("data/TMDB_tv_dataset_v3.csv", low_memory=False)
print("Linhas no arquivo original:", len(df))

limpo = df[
    (df["vote_count"] >= 10) &
    (df["episode_run_time"] > 0) &
    (df["number_of_episodes"] > 0) &
    (df["first_air_date"].notna()) &
    (df["genres"].notna())
]

colunas = [
    "name", "type", "status", "original_language", "genres", "origin_country",
    "number_of_seasons", "number_of_episodes", "episode_run_time",
    "vote_count", "vote_average", "popularity", "first_air_date"
]
limpo = limpo[colunas]

limpo.to_csv("data/series_limpo.csv", index=False)
print("Linhas depois da limpeza:", len(limpo))
