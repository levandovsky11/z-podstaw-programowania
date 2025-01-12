import os

def wyswietl(folder, poziom=0):
    try:
        elementy = os.listdir(folder)
    except PermissionError:
        print(" " * (poziom * 2) + "⛔ brak dostępu ⛔")
        return

    for element in elementy:
        sciezka = os.path.join(folder, element)
        if os.path.isdir(sciezka):
            print(" " * (poziom * 2) + f"📁{element}")
            wyswietl(sciezka, poziom + 2)
        else:
            print(" " * (poziom * 2) + f"📃{element}")

sciezka = input("podaj ścieżkę do folderu: ")
wyswietl(sciezka)


