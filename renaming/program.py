from PIL import Image
import PIL.ImageOps
import os

def invert(IN_PATH, OUT_PATH):
    start = int(input("Start: "))
    stop = int(input("Stop: "))
    for i in range(start, stop+1):
        in_path = IN_PATH + str(i) + ".png"
        out_path = OUT_PATH + str(i) + ".png"

        image = Image.open(in_path)

        inverted_image = PIL.ImageOps.invert(image)

        inverted_image.save(out_path)
        
    print('Execution Complete')

def rename(IN_PATH):
    files_imgs = sorted(os.listdir(IN_PATH))
    print(files_imgs)
    start = int(input("Start: "))
    ext = str(input("Extension: "))

    for f in files_imgs:
        os.rename(os.path.join(IN_PATH,f), os.path.join(IN_PATH, str(start) + ext))
        start += 1
    
    print('Execution Complete')

def main():
    print("What would you like to do?")
    print("1. Invert")
    print("2. Rename")

    inp = int(input("Option: "))

    IN_PATH = 'input'
    OUT_PATH = 'output'

    if (inp == 1):
        invert(IN_PATH, OUT_PATH)

    elif (inp == 2):
        rename(IN_PATH)

if __name__ == '__main__':
    main()
