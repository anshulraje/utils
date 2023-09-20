import os

def main():
    files_imgs = sorted(os.listdir(os.path.join('labels')))
    files_imgs = [(os.path.join('labels', f), f) for f in files_imgs]

    for i in range(len(files_imgs)):
        labels_path, file_name = files_imgs[i]
        edited_path = os.path.join("edited", file_name)

        f = open(labels_path, "r")

        lines = f.readlines()

        for j in range(0,len(lines)):
            first_char = lines[j][0]

            if first_char == "0":
                continue
            elif first_char == "1":
                lines[j] = lines[j].replace("1 ","0 ",1)
            elif first_char == "2":
                lines[j] = lines[j].replace("2 ","0 ",1)
        
        f_edited = open(edited_path, 'w+')
        for k in range(0,len(lines)):
            f_edited.write(lines[k])

if __name__ == "__main__":
    main()