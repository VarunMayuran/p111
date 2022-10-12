import os
import shutil

# .exe, .msi, .gif, .png, .jpg, .jpeg, .csv, .pdf, .xls, .xlsx, .ppt, .pptx

from_dir = "C:/Users/varun/Downloads"
to_dir = "C:/Users/varun/Downloaded Images"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image Files"
        path3 = path2 + '/' + file_name

        if os.path.exists(path2):
            print("Moving "+ file_name + "....")

            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("Moving "+ file_name + "....")
            shutil.move(path1,path3)
