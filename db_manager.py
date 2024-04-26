import pandas as pd
import csv
#importo il csv in un dataframe
df = pd.read_csv('Mars_crater_db_complete.csv')

#Creo un nuovo dataframe con solo le colonne di interesse
df = df[['CRATER_ID', 'LATITUDE_CIRCLE_IMAGE', 'LONGITUDE_CIRCLE_IMAGE', 'DIAM_CIRCLE_IMAGE', 'DEPTH_RIMFLOOR_TOPOG']]

#Rinomino le colonne
df.columns = ['id', 'lat', 'lon', 'diam', 'depth']

#funzione che filtra i crateri in base alla latitudine massima e minima passati per parametro
def filter_lat(db,lat_min, lat_max):
    return db[(db['lat'] >= lat_min) & (db['lat'] <= lat_max)]

#funzione che filtra i crateri in base alla longitudine massima e minima passati per parametro
def filter_lon(lon_min, lon_max):
    return df[(df['lon'] >= lon_min) & (df['lon'] <= lon_max)]

#funzione che filtra i crateri in base al diametro minimo
def filter_diam(db,diam_min):
    return db[(db['diam'] >= diam_min)]


def create_empty_csv(file_name, column_names):
    """
    Crea un file CSV vuoto con il nome specificato e le colonne corrispondenti ai nomi forniti.

    Args:
    - file_name: Il nome del file CSV da creare.
    - column_names: Una lista di stringhe contenenti i nomi delle colonne.
    """

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Scrive gli header con i nomi delle colonne
        writer.writerow(column_names)


def populate_csv(data):
    # Conta il numero di elementi prima dell'aggiunta dei nuovi dati
    before_count = 0
    with open('Mars_crater_db_images.csv', 'r') as f:
        before_count = sum(1 for line in f) - 1  # Sottrai 1 per l'intestazione

    existing_ids = set()
    with open('Mars_crater_db_images.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Salta l'intestazione
        for row in reader:
            existing_ids.add(row[0])  # Assume che l'ID sia il primo elemento di ogni riga

    with open('Mars_crater_db_images.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        added_count = 0  # Conta il numero di nuovi elementi aggiunti
        for id, image in data:
            if id not in existing_ids:
                writer.writerow([id, image])
                existing_ids.add(id)
                added_count += 1

    # Conta il numero di elementi dopo l'aggiunta dei nuovi dati
    after_count = 0
    with open('Mars_crater_db_images.csv', 'r') as f:
        after_count = sum(1 for line in f) - 1  # Sottrai 1 per l'intestazione

    print(f"Added {added_count} new entries. Total entries: {after_count} (before: {before_count})")