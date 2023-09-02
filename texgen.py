from PIL import Image
import math

path_prefix = input("Path prefix:\n")

path_list = input("Input paths, seperated by commas:\n").split(",")

w = int(input("New width:\n"))

h = int(input("New height:\n"))

texture_list = []

for path in path_list:
    loadIm = Image.open(path_prefix + path)

    im = loadIm.resize((w, h))

    texture = str(w).zfill(4) + str(h).zfill(4)

    rgb_im = im.convert("RGBA")
    for y in range(h):
        for x in range(w):
            if rgb_im.getpixel((x, y))[3] == 0:
                texture = texture + "---------"
            else:
                for k in range(3):
                    texture = texture + str(rgb_im.getpixel((x, y))[k]).zfill(3)

    texture_list.append(texture)
    print(path)

with open("output.txt", "w") as output:
    output.write("\n".join(texture_list))