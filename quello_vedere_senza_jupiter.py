import db_interactions as db_int
import image_manager as im
import coordinates_calcolator as cc
#%%
n, m, r = cc.coordinate_to_pixel_with_area(34.68,-132.517,65.49)
matrice = db_int.estrai_sotto_matrice(n, m, r)
im.visualizza_sotto_matrice(matrice)

#db_int.estrai_e_visualizza_sottomatrice(128,128,256)