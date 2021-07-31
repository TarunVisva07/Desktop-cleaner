import os
import re
import shutil
import time

print("Press Ctrl + C to stop any program .. :) ../..")


class DesktopInterface:

    def __init__(self, desktop):
        self.desktop = desktop
        self.files = list()
        for file in os.listdir(desktop):
            if "." in file:
                self.files.append(file)

    def show_files(self, ext):
        for file in self.files:
            if file.endswith("." + ext):
                print(file)

    def show_directories(self):
        i = 1
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
        return di

    def classify(self, ext, _dir):
        dst = os.path.join(self.desktop, _dir)
        try:
            os.mkdir(dst)
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

    def delete_dir(self, _dir):
        shutil.rmtree(os.path.join(self.desktop, _dir))
        print("The directory {} has been deleted successfully ...".format(_dir))


interface = DesktopInterface(input("Enter the path to your desktop"))
interface.get_files_by_extension()
while True:
    interface.classify(input("Enter extension"),input("Enter directory"))
    
