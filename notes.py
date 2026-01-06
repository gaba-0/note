import os

SCIEZKA = "notes_zap.txt"

class  notatka:
    def sparaw():
        os.path(SCIEZKA)
    def czetanie_pliku(self):
        with open("notes_zap.txt", "r", encoding="utf-8") as f:
            zawartosc = f.read()
            print("\n===== all records  =====")
            print(zawartosc)
            print("==============================\n")
        pass
    def wpisywanie_notatki(self):
        temat = input("Title??: ")
        sut = input("conten???: ")

        with open("notes_zap.txt", "a", encoding="utf-8") as zap:
            zap.write(f"\nTitle: {temat}\n")
            zap.write(f"content: {sut}\n")
            zap.write("----\n")
        pass
    def usuwanie(self):
        if not os.path.exists(SCIEZKA):
            print("There is no such record ")
            return
        




nott = notatka()
l = False
while not l: 
    print("\n===== MENU =====")
    print("\033[31m1.\033[0m aad records")
    print("\033[31m2.\033[0m show all records")
    print("\033[31m3.\033[0m exit")
    p1 = int(input("choose the required options by numbers:"))
    if p1 == 1:
        nott.wpisywanie_notatki()
    elif p1 == 2:
        nott.czetanie_pliku()
    elif p1 == 3:
        l = True



