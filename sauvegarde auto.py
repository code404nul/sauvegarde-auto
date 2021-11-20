import shutil
import os
import time
from tkinter.constants import Y

dem = int(input('entrez le chemin de votre disque dur externe'))
mo = int(input('si vous voulez deposer seulement un dossier tapez son chemin sinon ne faites rien '))

if os.path.exists('mo'):
    rep = mo
if dem <= 12:
    i = 0
    while i < 1000000:
        i = i + 1
        rep = rep + i 
        time.sleep (3)
        print("3")
        time.sleep (2)
        print("2")
        time.sleep(1)
        print("1")
        source = r'rep'
        destination = r'dem'
        shutil.move(source,destination)
        print("fichier transferer")
    else:
        print("erreur : réeseyer")

print("bonne journée")
print("jules h-c")  