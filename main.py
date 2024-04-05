import random


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
    with open('kitoblar.txt', 'r+') as kitoblar_royxati:
        with open("bandkitoblar.txt", "a+") as bandkitoblar:
        
            for i in kitoblar_royxati:
                print(i.strip().split())
            kitoblar_royxati.seek(0)
            a = input()
            if a in kitoblar_royxati.read():
                bandkitoblar.write(a)
                bandkitoblar.write("\n")
                print("Kitob olindi!")
                menyu()
              
#kitob berish
bandkitoblarlist = []
if InputNumber == 3:
    qaytaribberish = int(input("Kitobni id sini kitiring : "))
    with open('bandkitoblar.txt', 'r+') as kitoblar_royxati:
        for line in kitoblar_royxati:
            bandkitoblarlist.append(int(line.strip()))
        if qaytaribberish in bandkitoblarlist:
            bandkitoblarlist.remove(qaytaribberish)
            with open("bandkitoblar.txt", "w") as bandkitoblar:
                for i in bandkitoblarlist:
                    bandkitoblar.write(str(i) + "\n")
                    print("Kitob qaytarib berildi!")
        else:
            print("Kitob topilmadi!")

if  InputNumber == 4:
    with open("kitobxonlar.txt","r") as kitobxonlar:
        for i in kitobxonlar:
            print(i, end="")
            
if InputNumber == 5:
    with open("kitobxonlar.txt","a+") as kitobxonlar:
        new_kitobxon = input("Isminggizni kiriting : ")
        if new_kitobxon not in kitobxonlar:
            kitobxonlar.write("\n")
            kitobxonlar.write(new_kitobxon)
            print("Isminggiz royxatga qo'shildi!")
        else: 
            print("Bu royxatda bor!")
        
        
        