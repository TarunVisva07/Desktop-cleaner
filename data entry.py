import pickle
file_formats = {
    "ppt" : "PPTs",
    "pptx" : "PPTs",
    "docx" : "Word",
    "xlsx" : "Excel",
    "txt" : "Text files",
    "jpg" : "Images",
    "jpeg" : "Images",
    "png" : "Images",
    "pdf" : "PDFs",
    "py" : "Python programs",
    "java" : "Java programs",
    "class" : "Java programs",
    "c" : "C programs"
}
def add_data(file_formats):
    print("Exisiting file formats : ")
    for key,value in file_formats.items():
        print(key," : ",value)
    while True:
        if input("Do you want to add more data[y/n]?") == "n":break
        key,value = input("Enter extension"),input("Enter directory")
        if key in file_formats:
            if input("Are you sure you want replace existing folder name [y/n] ?") == "y":
                file_formats[key] = value
                continue
        file_formats[key] = value



def add_to_file():
    fp = open("File_formats.bin","rb")
    file_formats = pickle.load(fp)
    fp.close()
    add_data(file_formats)
    fp = open("File_formats.bin","wb")
    pickle.dump(file_formats,fp)
    fp.close()
    print("Data entry complete")

def initial_write():
    fp = open("File_formats.bin","wb")
    pickle.dump(file_formats,fp)
    fp.close()

if __name__ == "__main__":
    #initial_write()
    add_to_file()

    
        
        
    
