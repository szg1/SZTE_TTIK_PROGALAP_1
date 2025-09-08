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

#forint= <- változó definiálás
#input("") <- Felhasználói bemenet bekérése
# - idézőjelek közötti szöveg megjelenik a felhasználónak
forint=input("Hány forintod van? ")
#euro= <- változó definiálás
#int() <- típuskonverzió, a zárójelben lévő értéket átalakítja integer típusúvá
# / <- osztás
#370.0 <- lebegőpontos szám, az euró árfolyama
euro = int(forint) / 370.0
#print("") <- kiírás a képernyőre
# - a vesszővel elválasztott elemeket szóközzel választja el
print(forint,"forintból",euro,"euró-t tudsz vásárolni")