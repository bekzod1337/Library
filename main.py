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
            

if InputNumber == 2:
    with open('kitoblar.txt', 'r+') as kitoblar_royxati:
        with open("bandkitoblar.txt", "a+") as bandkitoblar:
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
#kitobxonlar royxati
if InputNumber == 4:
    ismlar = []
    with open("kitobxonlar.txt", "r") as kitobxonlar:
        for i in kitobxonlar:
            i = i.split(" ")
            print(i[0])

#kitobxon qoshish        
if InputNumber == 5:
    with open("kitobxonlar.txt","a+") as kitobxonlar:
        new_kitobxon = input("Isminggizni kiriting : ")
        if new_kitobxon not in kitobxonlar:
            kitobxonlar.write("\n")
            print("Isminggiz royxatga qo'shildi!")
            id = random.randint(1000,9999) 
            kitobxonlar.write(new_kitobxon + " ")   
            kitobxonlar.write(str(id))

#kitob qoshish
if InputNumber == 6:
    new_book_name = input("Kitob nomini kiriting : ")
    new_book_autor = input("Muallifni kiriting : ")
    new_book_id = str(random.randint(1000,9999))
    with open("Kitoblar.txt", "a+") as new_book:
        new_book.write("\n")
        new_book.write(str(new_book_name) + " ")
        new_book.write(str(new_book_autor) + " ")
        new_book.write(new_book_id)
        
if InputNumber == 7:
    print("Tashrifinggiz uchun rahmat!\nSog' bo'ling!")