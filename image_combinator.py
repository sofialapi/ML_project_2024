from PIL import Image
import io
import numpy as np


def fuse_images_horizontally(image_binaries):
    """
    Fonde insieme un elenco di immagini binarie orizzontalmente e restituisce la matrice risultante.

    Args:
    - image_binaries (list of bytes or str): Lista di immagini binarie codificate come stringhe binarie o oggetti bytes.

    Returns:
    - numpy.ndarray: Matrice risultante dalla fusione orizzontale di tutte le immagini.
    """

    # Funzione per convertire una stringa binaria o un oggetto bytes di immagine in una matrice NumPy
    def image_string_to_matrix(binary_data):
        if isinstance(binary_data, str):
            binary_data = binary_data.encode()
        img = Image.open(io.BytesIO(binary_data))
        img_array = np.array(img)
        return img_array

    # Converti tutte le immagini binarie in matrici NumPy
    matrices = [image_string_to_matrix(binary_data) for binary_data in image_binaries]

    # Verifica che tutte le matrici abbiano la stessa altezza
    heights = [matrix.shape[0] for matrix in matrices]
    if len(set(heights)) > 1:
        raise ValueError("Tutte le immagini devono avere la stessa altezza")

    # Affianca le matrici orizzontalmente
    combined_matrix = np.hstack(matrices)

    return combined_matrix


def string_to_bytes(binary_string):
    """
    Converte una stringa in un oggetto bytes-like.

    Args:
    - binary_string (str): Stringa da convertire in bytes.

    Returns:
    - bytes: Oggetto bytes-like corrispondente alla stringa binaria.
    """
    return binary_string.encode()