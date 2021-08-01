import os
import re
import shutil
import time
import pickle


class DesktopInterface:

    def __init__(self, desktop):
        self.desktop = desktop
        self.initialize_files()

    def initialize_files(self):
        self.files = list()
        for file in os.listdir(self.desktop):
            if "." in file:
                self.files.append(file)

    def show_files(self, ext):
        for file in self.files:
            if file.endswith("." + ext):
                print(file)

    def show_directories(self):
        i = 1
        print("DIRECTORIES :\n")
        for file in os.listdir(self.desktop):
            if "." not in file:
                print("{}. {}".format(i, file))
                i += 1

    def get_files_by_extension(self):
        li = [re.findall("\.(.+)", file)[0] for file in self.files]
        li = list(set(li))
        li.sort()
        di = dict()
        print("\n\n\nFILES BY EXTENSION : ")
        for x in li:
            i = 1
            print(x.upper(), ":")
            di[x.upper()] = list()
            for file in self.files:
                if file.endswith("." + x):
                    di[x.upper()].append(file)
                    print("{}. {}".format(i, file))
                    i += 1
            print()
        return di

    def classify(self, ext, _dir,root = None):
        if root == None:root = self.desktop
        dst = os.path.join(root, _dir)
        try:
            os.makedirs(dst)
            print("New directory created..")
            time.sleep(2)
        except FileExistsError:
            print("Directory already exists .... Moving there ")
            time.sleep(2)
            pass
            
        for file in self.files:
            if file.endswith("." + ext):
                src = os.path.join(self.desktop, file)
                try:
                    shutil.move(src, dst)
                    print("{} moved to {} successfully".format(file, _dir))
                except shutil.Error as e:
                    print("Unable to move {} due to {} error".format(file, e))
                    pass
                time.sleep(1.5)
        self.initialize_files()

    def auto_classify(self,root):
        fp = open("File_formats.bin","rb")
        file_formats = pickle.load(fp)
        fp.close()
        print("Warning!!! All types of files will be moved to respective folders under",root)
        if input("Press 'y' to proceed") == "y":
            for ext in file_formats:
                self.classify(ext,file_formats[ext],root)
        print("All files classified")

    def delete_dir(self, _dir):
        shutil.rmtree(os.path.join(self.desktop, _dir))
        print("The directory {} has been deleted successfully ...".format(_dir))

def displayMenu():
    menu = '''
    1.Show files by extension
    2.Show directories
    3.Organize files automatically
    4.Delete a directory
    5.Organize files manually
    '''
    print(menu)
    return int(input("Enter your choice (0 to exit application)"))
    
interface = DesktopInterface(input("Enter the path to your desktop"))

while True:
    ch = displayMenu()
    if ch == 0:
        break
    if ch == 1:
        interface.get_files_by_extension()
    elif ch == 2:
        interface.show_directories()
    elif ch == 3:
        interface.auto_classify(input("Enter path to root directory : "))
    elif ch == 4:
        interface.delete_dir("Enter directory name to delete : ")
    elif ch == 5:
        interface.classify(input("Enter extension : "),input("Enter directory name : "))
    else:
        print("Invalid choice ")

print("\nThank you for using this application :)")


    
