#!/usr/bin/python3

"""
COPYRIGHT NOTICE
This file was written by Szabó Gergő - https://github.com/szg1
You are allowed to use it in your own projects
You are allowed to modify it to suit your needs
You are required to keep this notice in the file
You are NOT allowed to publish it as your own work
You are NOT allowed to use it for commercial purposes
If you find any bugs, please report them to the author
"""

# def valami() <- függvény definiálása
# -> visszatérési típus (ha van)
# -> None <- nincs visszatérési érték
def main() -> None: # főprogram definiálása
    #forint:str <- str típusú változó definiálása
    #input("") <- felhasználói bemenet bekérése
    # - idézőjelek közötti szöveg megjelenik a felhasználónak
    forint:str = input("Hány forintod van? ") # felhasználói bemenet bekérése
    #forint_szam:int <- int típusú változó definiálása
    #int() <- típuskonverzió, a zárójelben lévő értéket átalakítja integer típusúvá
    forint_szam:int = int(forint) # stringből integer típusúvá alakítás
    #euro:float <- float típusú változó definiálása
    #forint_szam / 370.0 <- osztás, az euró árfolyama
    euro:float = forint_szam / 370.0 # átváltás
    #print(f"") <- formázott kiírás a képernyőre
    # - a kapcsos zárójelek között lévő változók értékei kerülnek beillesztésre
    # - :.2f <- lebegőpontos szám, 2 tizedesjeggyel
    print(f"{forint_szam} forintból {euro:.2f} euró-t tudsz vásárolni") # eredmény kiírása

# feltétel: ha a fájlt programként futtatod
if __name__ == "__main__": # ha programként futtatod
    # main függvény meghívása
    main() # főprogram meghívása
