import pandas as pd;

df=pd.read_csv("spotify_data.csv")

#print(df.columns.tolist())

columns=df[['artist_name', 'track_name', 'popularity', 'year', 'genre', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'duration_ms', 'time_signature']]
#Lo siguiente quita la notacion cientifica de las columnas, para evitar problemas de formatos al subir a elasticsearch
columns['instrumentalness'] = columns['instrumentalness'].apply(lambda x: float(f"{x:.8f}"))
columns['acousticness'] = columns['acousticness'].apply(lambda x: float(f"{x:.8f}"))

columns.to_json('soptify_data.json',orient='records', lines=True)

print("Proceso de conversion terminado")