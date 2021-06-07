from os import path
import re
from enum import IntEnum
import time
import os, io
import sys
from pathlib import Path
import shutil
import glob

baza_plikow = []
copyFile = []
badFile = []
noFile = {}
foto = []
end_mask = "^x$"
picture_mask = "^DSC_[0-9]{1,8}.JPG$"
fok_mask = "^FOK_[0-9]{1,8}.JPG$"
index_mask = "DSC_"
fok_index_mask = "FOK_"
prefix_mask = ".JPG"
number_mask = "^[1-9]$"
wybor_mask = "^[1-4]{1,1}$"
error_mask = "^[a-zA-Z]$"
symbol_mask = "^[a-zA-Z]{1,1}[0-9]{1,2}$"
picture = 0
pictures = 0
number = 0

#PC path
pcpathrap = ("c:/Users/mstep/iCloudDrive/Programowanie/Python_file/Raporty/raport.txt")
pcpathdirrap = ("c:/Users/mstep/iCloudDrive/Programowanie/Python_file/Raporty")
pcpathmachine = ("c:/Users/mstep/iCloudDrive/Programowanie/Python_file/pictures/na_maszyne")
pcbasepath = ("c:/Users/mstep/iCloudDrive/Programowanie/Python_file/pictures//*/gotowe")
# macpath
macpatchrap = ("/Volumes/TOSHIBA EXT/Zrobione/Raporty/raport.txt")
macpathdirrap = ("/Volumes/TOSHIBA EXT/Zrobione/Raporty")
macpathmachine = ("/Volumes/TOSHIBA EXT/Zrobione/na_maszyne")
macbasepath = ("/Volumes/TOSHIBA EXT/Zrobione/")
fotopath = ("//*")

localtime = time.asctime(time.localtime(time.time()))

def main():
    print()
    print("************ Wyszukiwatce zdjęć **************")
    print("************ Firma Fotograficzna FOKUS **************")
    menu()

def menu():
    
    localtime = time.asctime( time.localtime(time.time()))

    choice = input("""
                    1. Dodaj nr zdjęcia

                    2. Podgląd listy - kasuj zdjęcie

                    3. Wuszukaj, skopiuj, zapisz raport

                    4. Zakończ program

                      Jaki jest Twój wybór: """)

    if choice == "1": # Dodawanie plików
        addpictures()

    elif (choice == "2"): # Usuwanie plików
        delettepictures()

    elif (choice == "3"): # Wyszukiwanie plików oraz kopiowanie ich do katalogu
        findpictures()
    
    elif (choice == "4"): # Zapisywanie raportów
        exit()    
    
    else:
        print("Musisz wybrać numer od 1 do 4")
        print("Powtórz")
        menu()

def addpictures():  # dodawanie plików
    picture = 0  
    while picture != end_mask:
        print("UWAGA!!! Wpisz (x) aby wrócić do MENU")
        #foto = input("Podaj symbol fotografa ")
        data = input("Podaj numer pliku .jpg:  ")
        #Połączenie nr pliku z prefixem i rozszerzeniem pliku
        picture = index_mask + data + prefix_mask
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
            menu()
        else:
            print()
            print("UWAGA!!! Wpisałeś błędny numer pliku. ")
            print()
            pass
    # Za pierwszym uruchomieniem programu gdy do bazy zostanie dopisany dwa lub więcej razy,
    # ten sam plik, będzie on wyświetlony tyle razy ile został dopisany ale tylko raz skopiowany na maszynę.

def delettepictures():  # Usuwanie plików
    picture = 0
    while picture != end_mask:
            
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
            print("lub wpisz (x) - aby wrócić do MENU")
            print()

            picture = input("Jaki jest Twój wybór?  ")
            #picture = index_mask+picture+prefix_mask
            print("UWAGA!!! Wpisałeś numer ",picture)
            if picture in baza_plikow:
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
            elif re.match(end_mask, picture):
                menu()
            else:
                print()
                print ("UWAGA!!! Nie ma takiego pliku... ")

def findpictures(): # wyszukiwanie plików
    
    if not os.path.exists(macpathmachine):
        os.makedirs(macpathmachine)

    fotoindex = input("Podaj symbol fotografa ")
    def fotosymbol(fotomen):
        foto.append(fotomen)
    fotosymbol(fotoindex)

    for sphoto in foto:

        if re.match(symbol_mask, sphoto):
            basepath = macbasepath + sphoto + fotopath
            machine_path = (macpathmachine)

            for file in baza_plikow:
                #print(file)
                pathfile = glob.glob(os.path.join(basepath, file))
                print(pathfile)
                for file in pathfile:
                    shutil.copy(file, machine_path)
                    
                    (filepath, filename) = os.path.split(file) #rozbijanie ścieżki i nazwy pliku
                    #print("Plik", filename, "skopiowany do folderu na maszynę")

                    def addcopyfile(parametrfunkcji):
                        copyFile.append(parametrfunkcji)
                        for i, v in enumerate(copyFile):
                            i += 1
                            print("Znaleziono plik ")
                            print("[",i,"]", v)
                            print()
                    # Przesłanie parametru do funkcji
                    addcopyfile(filename)
        else:
            print("Wpisałeś błędny symbol fotografa! ") 
            foto.clear()
            menu()
        
    # W wyniku działania "set" powstaje słownik, który konwertuję na listę..   
    noFile = set(baza_plikow) - set(copyFile)
    noFile = list(noFile)
    for picture in noFile:
        def noCopyFile(params):
            badFile.append(params)
        noCopyFile(picture)

    print("Pliki przekazane do wyszukania !", baza_plikow)
    print("Tych plików nie znaleziono !!", badFile)
    print("Pliki skopiowane na maszyne !!!", copyFile)
    
    #menu()
    rapwrite()
    
def rapwrite(): # zapisywanie raporu
    # Sprawdzenie czy katalog i plik iztnieje
    for sphoto in foto:
       
        if os.path.exists(macpatchrap):
            print()
            with open(macpatchrap, "a+", encoding="UTF8") as file:
                file.write("------------------------\n")
                file.write(localtime + "\n")
                file.write(str(sphoto) + "\n")
                for picture in copyFile:
                    try:
                        file.write(picture + " (Plik skopiowano na maszynę)\n")
                    except IndexError:
                        file.write("\n")
                        print("plik dodany")
                for picture in badFile:
                    try:
                        file.write(picture + " (Pliku nie znaleziono)\n")
                    except IndexError: 
                        file.write("\n")   
            print()            
            print("Raport zapisany", localtime)   
            baza_plikow.clear()
            badFile.clear()
            copyFile.clear()
            foto.clear()
        elif not os.path.exists(macpathdirrap):
            print("plik nie istnieje")
            print("TWORZĘ NOWE RAPORTY.TXT")
            #path = ("./Raporty")
            os.makedirs(macpathdirrap)
            with open(macpatchrap, "w", encoding="UTF8") as file:
                file.write("------------------------\n")
                file.write(localtime + "\n")
                file.write(str(sphoto) + "\n")
                for picture in copyFile:
                    try:
                        file.write(picture + " (Plik skopiowano na maszynę)\n")
                    except IndexError:
                        file.write("\n")
                        print("plik dodany")
                for picture in badFile:
                    try:
                        file.write(picture + " (Pliku nie znaleziono)\n")
                    except IndexError: 
                        file.write("\n")        
            print()            
            print("Raport zapisany", localtime) 
            print() 
            baza_plikow.clear()
            badFile.clear()
            copyFile.clear()
            foto.clear()
        menu()
     
def exit():
    print("Do zobaczenia")
    sys.exit() # Zakończenie programu
main()  