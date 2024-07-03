import io
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

def visualizza_sotto_matrice(sotto_matrice):
    # Converti la sotto-matrice in un'immagine PIL
    immagine = Image.fromarray(np.uint8(sotto_matrice), 'L')  # 'L' indica che l'immagine è in scala di grigi

    # Visualizza l'immagine utilizzando matplotlib
    plt.imshow(immagine, cmap='gray')  # Usa la mappa dei colori 'gray' per visualizzare l'immagine in scala di grigi
    plt.axis('off')  # Nasconde gli assi
    plt.show()


def salva_sotto_matrice_come_png(sotto_matrice, nome_file, cartella_destinazione):
    # Verifica se la cartella di destinazione esiste, altrimenti la crea
    if not os.path.exists(cartella_destinazione):
        os.makedirs(cartella_destinazione)

    # Costruisce il percorso completo del file
    percorso_completo = os.path.join(cartella_destinazione, nome_file)

    # Converte la matrice in immagine e la salva
    immagine = Image.fromarray(np.uint8(sotto_matrice))
    immagine.save(percorso_completo)