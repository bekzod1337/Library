import random



print("Assalomu alaykum!\n")
print("1. Kitoblar ro'yxati")
print("2. Kitob berish")
print("3. Kitobni qaytarib berish")
print("4. Kitobxonlar Ro'yxati")
print("5. Kitobxon qo'shish")
print("6. Kitob qo'shish")
print("7. Chiqish")
InputNumber = int(input("Quyidagilardan birini (raqamini) kiriting : "))
if InputNumber == 1:
    with open('kitoblar.txt', 'r+') as kitoblar_royxati:
        kitoblar_royxati.seek(0)
        for i in kitoblar_royxati:
            print(i.strip().split())
            
        a = input()
        if a in kitoblar_royxati.read():
            print("Success")
        
elif InputNumber == 2:
    pass