import random
from KitoblarRoyxati import KitoblarRoyxati
from KitobOlish import Kitob_olish
from KitobQaytaribBerish import Kitob_Berish
from Kitobxonlar import Kitobxonlar
from KitobxonQoshish import KitobxonQoshish
from KitobQoshish import KitobQoshish
from menyu import menyu

while True:
    InputNumber = 0
    InputNumber =  menyu.show_menyu()
    #kitoblar ro'yxati
    if InputNumber == 1:
        KitoblarRoyxati.Kitoblar_royxati()     
    #kitob berish
    if InputNumber == 2:
        Kitob_olish.kitobolish() 
    #kitobni qaytarib berish
    if InputNumber == 3:
        Kitob_Berish.kitob_berish()
    #kitobxonlar royxati
    if InputNumber == 4:
        Kitobxonlar.kitobxonlar_royxati()
    #kitobxon qoshish        
    if InputNumber == 5:
        KitobxonQoshish.Kitobxon_qoshish()
    #kitob qoshish
    if InputNumber == 6:
        KitobQoshish.Kitob_Qoshish()
    #chiqish
    if InputNumber == 7:
        print("Tashrifinggiz uchun rahmat!\nSog' bo'ling!")
        break