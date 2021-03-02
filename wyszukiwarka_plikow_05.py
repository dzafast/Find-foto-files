import re
from enum import IntEnum

baza_plikow = []
end_mask = "^end$"
picture_mask = "^DSC[0-9]{1,8}.jpg$"
index_mask = "DSC"
prefix_mask = ".jpg"
number_mask = "^[1-9]$"
wybor_mask = "^[1-4]{1,1}$"
error_mask = "^[a-zA-Z]$"
picture = 0
number = 0

while(True):

    menu = IntEnum('menu', 'add delete find end read')
    print()

    wybor = int(input("""Dokonaj wyboru!:
    1. Dodaj nr zdjęcia
    2. usuń zdjęcie z listy
    3. Wuszukaj i zkopiuj
    4. Zakończ i zapisz raport
    5. Wczytaj z pliku txt
    """))

    if (wybor == menu.add):
        while picture != end_mask:
            print("Wpisz end aby wrócić do MENU")
            data = input("Podaj numer pliku .jpg:  ")
            #Połączenie nr pliku z prefixem i rozszerzeniem pliku
            picture = index_mask+data+prefix_mask

            #Porównanie pliku ze wzorcem wyrażenia regularnego
            if re.match(picture_mask, picture):
                print()
                print("Dodano do bazy!")

                #funkcja dodająca nazwę pliku do tablicy
                def addPictures(parametrFunkcji):
                    baza_plikow.append(parametrFunkcji)
                    for i, v in enumerate(baza_plikow):
                        i += 1
                        print("[",i,"]", v)
                    print()

                #Przesłanie parametru do funkcji
                addPictures(picture)

            elif re.match(end_mask, data):
                break
            else:
                print()
                print("UWAGA!!! Wpisałeś błędny numer pliku. ")
                print()

    elif (wybor == menu.delete):
        while picture != "end":
            print()
            ilosc = len(baza_plikow)
            print("Zapisanych plików : ", ilosc)
            print()

            if ilosc < 1:
                print("UWAGA!!! W bazie nie ma jeszcze żadnych plików!")
                break
            else:
                #Zliczenie wszystkich plików w tablicy
                for i, v in enumerate(baza_plikow):
                    i += 1
                    print("[",i,"]", v)

                print()
                print("Podaj numer zdjęcia które chcesz usunąć!")
                print()
                print("lub wpisz end - aby wrócić do MENU")
                print()

                picture = input("Jaki jest Twój wybór?  ")
                #picture = index_mask+picture+prefix_mask
                print("UWAGA!!! Wpisałeś numer ",picture)

                print("Czy na pewno chcesz usunąć plik", picture)
                
                if re.match(picture_mask, picture):
                    delete = input("UWAGA!!! Wpisz /y/ jesli tak! lub /n/ jesli nie! ")
                    if (delete == "y"):

                        def deletePicture(deleteFile):

                            baza_plikow.remove(deleteFile)
                            print()
                            print("Plik, ", (deleteFile), " został usunięty!")
                        deletePicture(picture)
                        
                    elif (delete == "n"):
                        break
                    else:
                        print()
                        print ("UWAGA!!! Nie ma takiego pliku... ")
                elif re.match(end_mask, picture):
                    break
    else:
        print("Nie prawidłowy wybór, wybierz jeszcze raz!")
