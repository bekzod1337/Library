class Kitob_olish:
    def kitobolish():
        with open('kitoblar.txt', 'r+') as kitoblar_royxati:
            with open("bandkitoblar.txt", "a+") as bandkitoblar:
                kitoblar_royxati.seek(0)
                a = input("Kitob nomini kiriting : ")
                if a in kitoblar_royxati.read():
                    bandkitoblar.write(a)
                    bandkitoblar.write("\n")
                    print("Kitob olindi!")
                    menyu()
                else:
                    print("Bunday kitob mavjud emas")