import math

#8192x32768, 45,-180
"""
def lat_lon_to_tile(lat, lon, zoom):
    n = 2 ** zoom
    lat_rad = math.radians(lat)
    xtile = int((lon + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile


def lat_lon_to_tile_cil(lat, lon, zoom):
    n = 2 ** zoom
    x = (lon + 180.0) / 360.0 * n
    y = (1.0 - math.sin(math.radians(lat))) / 2.0 * n
    return int(x), int(y)
"""

def meters_to_degrees(meters, radius):
    """Converte una distanza in metri in gradi su un pianeta con un dato raggio."""
    # Circonferenza del pianeta
    circumference = 2 * math.pi * radius
    # Converti metri in frazione di circonferenza
    fraction_of_circumference = meters / circumference
    # Converti frazione di circonferenza in gradi (360° in una circonferenza completa)
    degrees = fraction_of_circumference * 360
    return degrees


def coordinate_to_pixel_with_area(lat, lon, length_meters, mars_radius=3389.5e3):
    # Dimensioni dell'immagine
    height = 8192
    width = 32768

    # Limiti delle coordinate
    max_lat = 45.0
    min_lat = -45.0
    max_lon = 180.0
    min_lon = -180.0

    # Calcolare la posizione y (riga) del pixel centrale
    y_center = int((max_lat - lat) / (max_lat - min_lat) * height)

    # Calcolare la posizione x (colonna) del pixel centrale
    x_center = int((lon - min_lon) / (max_lon - min_lon) * width)

    # Converti lunghezza in metri a gradi di latitudine/longitudine
    degrees_length = meters_to_degrees(length_meters*500, mars_radius)

    # Calcolare la distanza in pixel
    pixels_per_degree_lat = height / (max_lat - min_lat)
    pixels_per_degree_lon = width / (max_lon - min_lon)

    pixels_lat = degrees_length * pixels_per_degree_lat
    pixels_lon = degrees_length * pixels_per_degree_lon

    # Arrotondare al numero intero più vicino
    side_length_pixels = int(max(pixels_lat, pixels_lon))

    return y_center, x_center, side_length_pixels