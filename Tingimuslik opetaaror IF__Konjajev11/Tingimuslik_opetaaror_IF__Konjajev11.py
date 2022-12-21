from math import*
from random import*

while True:
    nimi=input("Mis sinu nimi on?: ")
    if nimi.isalpha(): break
if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled?: "))
            break
        except:
            print("On vaja arvude tüüp kasutada")
    if 0<vanus<6:
        print("Tasuta")
    elif 6<=vanus<=14:
        print("Lastepilet")
    elif 15<=vanus<=65:
        print("Täispilet")
    elif 65<=vanus<100:
        print("Sooduspilet")
    else:
        print("Vanus ei soobi!")
else:
     print("Ma otsin Juku!")

print()