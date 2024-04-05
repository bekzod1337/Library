class Kitobxonlar:
    def kitobxonlar_royxati():
        ismlar = []
        with open("kitobxonlar.txt", "r") as kitobxonlar:
            for i in kitobxonlar:
                i = i.split(" ")
                print(i[0])