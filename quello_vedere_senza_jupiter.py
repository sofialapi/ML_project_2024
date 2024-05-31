import db_interactions as db_int
import image_manager as im
#%%
matrice= db_int.estrai_sotto_matrice(256,256,512)
im.visualizza_sotto_matrice(matrice)

#db_int.estrai_e_visualizza_sottomatrice(128,128,256)