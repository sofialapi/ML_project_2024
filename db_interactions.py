import sqlite3
import numpy as np


def estrai_sotto_matrice(n, m, l, nome_db="matrice_pixel.db"):
    try:
        conn = sqlite3.connect(nome_db)
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(f"Errore di connessione al database: {e}")
        return None

    half_l = l // 2
    start_x = n - half_l
    end_x = n + half_l
    start_y = m - half_l
    end_y = m + half_l

    sotto_matrice = np.zeros((l, l), dtype=int)  # Modificato per gestire un solo canale

    try:
        cur.execute('''
               SELECT x, y, value FROM pixels  -- Modificato per selezionare solo il valore di intensità
               WHERE x BETWEEN ? AND ? AND y BETWEEN ? AND ?
           ''', (start_x, end_x, start_y, end_y))
    except sqlite3.Error as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        conn.close()
        return None

    rows = cur.fetchall()

    # Debugging: log the fetched rows
    print("Numero di righe estratte:", len(rows))
    if len(rows) > 0:
        print("Prime 10 righe estratte:", rows[:10])  # Log only the first 10 rows for brevity

    for row in rows:
        try:
            x, y, value = row
            x = int(x)
            y = int(y)
            value = int(value)  # Converti il valore di intensità in intero
            if 0 <= x - start_x < l and 0 <= y - start_y < l:
                sotto_matrice[x - start_x, y - start_y] = value
        except ValueError as e:
            # Logga l'errore e la riga problematica
            print(f"Errore durante la conversione dei dati: {e}")
            print(f"Riga problematica: {row}")

    conn.close()

    return sotto_matrice


def estrai_e_visualizza_sottomatrice(n, m, l, nome_db="matrice_pixel.db"):
    conn = sqlite3.connect(nome_db)
    cur = conn.cursor()

    half_l = l // 2
    start_x = n - half_l
    end_x = n + half_l
    start_y = m - half_l
    end_y = m + half_l

    sotto_matrice = np.zeros((l, l, 3), dtype=int)

    cur.execute('''
        SELECT x, y, value FROM pixels
        WHERE x BETWEEN ? AND ? AND y BETWEEN ? AND ?
    ''', (start_x, end_x, start_y, end_y))

    rows = cur.fetchall()

    for row in rows:
        x, y, value = row
        x = int(x)
        y = int(y)
        value = int(value)
        if 0 <= x - start_x < l and 0 <= y - start_y < l:
            sotto_matrice[x - start_x, y - start_y] = value

    conn.close()

    # Visualizza la sottomatrice come matrice numerica
    print("Sottomatrice:")
    print(sotto_matrice)