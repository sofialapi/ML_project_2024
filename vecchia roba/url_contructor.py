base_mars_url  = "https://trek.nasa.gov/tiles/Mars/EQ/msss_atlas_simp_clon/1.0.0//{Style}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}.png"


def get_request_url(lat, lon, url=None, style='default', tileMatrixSet='default028mm', tileMatrix='6'):

    if url is None:
        url = base_mars_url.format(
            Style=style,  # Stile del tile (può essere diverso, controlla il documento XML per il valore corretto)
            TileMatrixSet=tileMatrixSet,  # Set di matrici di tile (controlla il documento XML per il valore corretto)
            TileMatrix=tileMatrix,  # Matrice di tile (può essere diversa, controlla il documento XML per il valore corretto)
            TileRow=lat,  # Riga del tile
            TileCol=lon  # Colonna del tile
        )
        return url
    else:
        raise ValueError("ancora non implementato")