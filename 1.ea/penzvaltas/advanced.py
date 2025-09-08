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
def main() -> None: # főprogram definiálása
    forint:str = input("Hány forintod van? ") # felhasználói bemenet bekérése
    forint_szam:int = int(forint) # stringből integer típusúvá alakítás
    euro_arfolyam:float = 370.0 # az euró árfolyama
    euro:float = forint_szam / euro_arfolyam # átváltás
    print(f"{forint_szam} forintból {euro:.2f} euró-t tudsz vásárolni") # eredmény kiírása

if __name__ == "__main__": # ha programként futtatod
    main() # főprogram meghívása
