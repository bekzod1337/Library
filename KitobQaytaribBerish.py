# from main import main

class Kitob_Berish:
    def kitob_berish():
        bandkitoblarlist = []
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