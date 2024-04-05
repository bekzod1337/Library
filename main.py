import random
from KitoblarRoyxati import KitoblarRoyxati
from KitobQaytaribBerish import Kitob_Berish
from KitobOlish import Kitob_olish
from Kitobxonlar import Kitobxonlar
from KitobxonQoshish import KitobxonQoshish
from KitobQoshish import KitobQoshish
def menyu():
    print("Assalomu alaykum!\n")
    print("1. Kitoblar ro'yxati")
    print("2. Kitob berish")
    print("3. Kitobni qaytarib berish")
    print("4. Kitobxonlar Ro'yxati")
    print("5. Kitobxon qo'shish")
    print("6. Kitob qo'shish")
    print("7. Chiqish")
    InputNumber = int(input("Quyidagilardan birini (raqamini) kiriting : "))
    return InputNumber

InputNumber = 0
InputNumber =  menyu()

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