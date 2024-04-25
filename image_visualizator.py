import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def image_visualizator_from_bin(image_data):
    image_file = io.BytesIO(image_data)

    # Carica l'immagine
    img = mpimg.imread(image_file)

    # Visualizza l'immagine
    plt.imshow(img)
    plt.axis('off')  # Disabilita gli assi
    plt.show()