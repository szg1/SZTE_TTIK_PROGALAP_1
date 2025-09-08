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
# Nagybetűs változók: konstansok (nem változnak a program futása során)
# - A python nem tiltja meg a módosításukat, de a programozói konvenciók szerint
#   nem szabad megváltoztatni őket
HUFEUR = 370.0 # globális változó, az euró árfolyama

# függvénydefiníció
# () <- paraméterek
# forint:int, arfolyam:float <- típusmegkötések
# -> float <- visszatérési érték típusa
def valtas(forint:int, arfolyam:float) -> float: # függvény definiálása
    """Forintot euróra vált az adott árfolyamon"""
    # if: feltétel
    # - feltétel: az árfolyam nem lehet nulla
    if arfolyam == 0.0: # az árfolyam nem lehet nulla
        # raise: kivétel dobása, a program leáll, és kiírja a hibát
        raise ValueError("Az árfolyam nem lehet nulla!") # hibakezelés
    # return: visszatérési érték
    return forint / arfolyam # átváltás

def main() -> None: # főprogram definiálása
    forint:str = input("Hány forintod van? ") # felhasználói bemenet bekérése
    forint_szam:int = int(forint) # stringből integer típusúvá alakítás
    euro:float = valtas(forint_szam, HUFEUR) # átváltás függvénnyel
    print(f"{forint_szam} forintból {euro:.2f} euró-t tudsz vásárolni") # eredmény kiírása

if __name__ == "__main__": # ha programként futtatod
    main() # főprogram meghívása