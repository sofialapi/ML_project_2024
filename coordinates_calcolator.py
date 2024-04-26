import math

def lat_lon_to_tile(lat, lon, zoom):
    n = 2 ** zoom
    lat_rad = math.radians(lat)
    xtile = int((lon + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile


#coordinate_conversion prende lat, lon e restituisce la tile_row e tile_column in cui si trova
def coordinate_conversion(lat, lon):
    # Calculate row index
    tile_row = int((lat + 45) * (47 - 16) / 90) + 16

    # Calculate column index
    tile_col = int((lon + 180) * (127) / 360)

    return tile_row, tile_col
