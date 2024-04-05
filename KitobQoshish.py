import random

class KitobQoshish:
    def Kitob_Qoshish():
        new_book_name = input("Kitob nomini kiriting : ")
        new_book_autor = input("Muallifni kiriting : ")
        new_book_id = str(random.randint(1000,9999))
        with open("Kitoblar.txt", "a+") as new_book:
            new_book.write("\n")
            new_book.write(str(new_book_name) + " ")
            new_book.write(str(new_book_autor) + " ")
            new_book.write(new_book_id)
