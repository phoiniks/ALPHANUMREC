#!/usr/bin/python
from sys import argv
from os.path import splitext
import imageio
import cv2


def visualize(img):
    img = imageio.imread(img)
    width = img.shape[0]
    for row1 in img: 
        count = 0 
        for row2 in row1: 
            count += 1
            s = sum(row2)
            # if s != 0 and s != 765:
            #     s = 0
            print("{0:3d}".format(s), end="") 
            if count % width == 0: 
                print()


                
def rot90(img):
    img = cv2.imread(img)
    timg = cv2.transpose(img)
    timg = cv2.flip(timg, flipCode = 1)
    name, ext = splitext(argv[1])
    print(name)
    resultat = name + "_rotiert" + ext
    cv2.imwrite(resultat, timg)



if __name__ == "__main__":
    img = argv[1]
    visualize(img)

    antwort = input("Bild um 90 Grad drehen? (j oder n)")
    if antwort == "j":
        print("Erzeuge um 90 Grad im Uhrzeigersinn gedrehte Kopie von {}.".format(argv[1]))
        rot90(img)
