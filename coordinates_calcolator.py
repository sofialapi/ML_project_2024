import math

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