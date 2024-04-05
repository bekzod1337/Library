import random
class KitobxonQoshish:
    def Kitobxon_qoshish():
        with open("kitobxonlar.txt","a+") as kitobxonlar:
            new_kitobxon = input("Isminggizni kiriting : ")
            if new_kitobxon not in kitobxonlar:
                kitobxonlar.write("\n")
                print("Isminggiz royxatga qo'shildi!")
                id = random.randint(1000,9999) 
                kitobxonlar.write(new_kitobxon + " ")   
                kitobxonlar.write(str(id))