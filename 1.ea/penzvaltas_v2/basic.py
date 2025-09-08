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

HUFEUR = 390.0

def valtas(forint,arfolyam):
    return forint / arfolyam

def main():
    forint = float(input("Hány forintod van? "))
    print(f"{forint:.2f} forintból {valtas(forint,HUFEUR):.2f} euró-t tudsz vásárolni")

if __name__ == "__main__":
    main()