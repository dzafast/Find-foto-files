import re
from enum import IntEnum

baza_plikow = []
end_mask = "^end$"
picture_mask = "^DSC[0-9]{1,8}.jpg$"
index_mask = "DSC"
prefix_mask = ".jpg"
picture = 0
number = 0

while(True):

    menu = IntEnum('menu', 'add show delete find end')
    wybor = int(input("""Dokonaj wyboru!:
    1. Dodaj nr zdjęcia
    2. Pokaż wszystkie
    3. Usuń zdjęcie
    4. Wyszukaj
    5. Zakończ i zapisz
    """))

    if (wybor == menu.add):

        while picture != end_mask:
            print("Wpisz end aby wrócić do MENU")
            data = input("Podaj numer pliku .jpg:  ")
            picture = index_mask+data+prefix_mask
            if re.match(picture_mask, picture):
                print()
                print("plik poprawny!")
                print()
                baza_plikow.append(picture)
                print(baza_plikow)

            elif re.match(end_mask, data):
                break

            else:
                print()
                print("Wpisałeś błędny numer pliku! ")
                print()

    elif (wybor== menu.show):
        
        while picture != end_mask:

            for i in baza_plikow:
                number += 1
                print(number, i)
            print("end - powrót do MENU")
            print()
            data = input("wpisz ...  ")
            if re.match(end_mask, data):
                break
            
        

        

        

           

