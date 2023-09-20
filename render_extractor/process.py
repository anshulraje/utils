import cv2
import os
from PIL import Image
import numpy as np

def importer(PATH_MAIN):
    files = sorted(os.listdir(os.path.join(PATH_MAIN)))
    files = [os.path.join(PATH_MAIN, f) for f in files]
    return files

def extractor(video):
    frames = []

    fc = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print('frame count =',fc)

    for i in range(fc):
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = video.read()

        if ret:
            frames.append(frame)
        else:
            print("Frame not found")

    for i in range(len(frames)):
        cv2.imwrite('output/frames/%i.png' % i, frames[i])

    print("Frame Extraction Complete") 

def png_and_mask_generator():
    images = importer("output/frames")

    for i in range(len(images)):
        print("Iteration %i" % i)

        img = Image.open(images[i])
        img = img.convert('RGBA')
        datas = img.getdata()

        newData = []
        newData_mask = []
        for item in datas:
            if (item[0] <= 113 and item[1]>230 and item[1]<=255 and item[2] <= 113) or (item[0] <= 15 and item[1]>150 and item[1]<=255 and item[2] <= 15):
                newData.append((0, 254, 0, 0))
                newData_mask.append((255,255,255,255))
            else:
                newData.append(item)
                newData_mask.append((0,0,0,255))

        img.putdata(newData)
        img.save("output/images/%i.png" % i, "PNG")
        
        img.putdata(newData_mask)
        img.save("output/masks/%i.png" % i, "PNG")
    
    print("PNG & Mask Generation Complete")


def main():
    files = importer("input")

    video = cv2.VideoCapture(files[0])

    extractor(video)

    png_and_mask_generator()



if __name__ == "__main__":
    main()