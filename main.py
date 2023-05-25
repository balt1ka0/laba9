import os
from PIL import Image, ImageFilter
import csv


def z1_2():
    rez = sorted(os.listdir(path="img"))
    ex = ['jpeg', 'jpg']
    for n, item in enumerate(rez):
        if item.split('.')[-1] in ex:
            with Image.open("img/"+item) as img:
                new_img= img.filter(ImageFilter.EMBOSS)
                try:
                    os.mkdir('new_img')
                except:
                    pass
                new_img.save(r'D:\UserFolders\Desktop\лаба9\new_img\img_new'+item)

z1_2()


def z3():
    with open("data.csv", "r") as r_file:
        file_reader = list(csv.reader(r_file, delimiter=","))
    print("Нужно купить:")
    for i in file_reader:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in file_reader])} руб.")
