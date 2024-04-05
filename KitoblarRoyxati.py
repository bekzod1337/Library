class KitoblarRoyxati:
    def Kitoblar_royxati():
        with open('kitoblar.txt', 'r+') as kitoblar_royxati:
            with open("bandkitoblar.txt", "a+") as bandkitoblar:
                for i in kitoblar_royxati:
                    print(i.strip().split())