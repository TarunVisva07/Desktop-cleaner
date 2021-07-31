# Desktop-cleaner

In this pandemic situation where most of our daily events are happening virtually , most of us use a computer/laptop everyday for online classes,work from home etc..
As a result we end up with a lot of files in our desktop which makes it look a little rubbish. Being an Engineering student 
my desktop looked the same, flooded with lots of pdfs,books,ppts,images etc.. scattered here and there. Creating a folder for different types of files and moving
files into the respective folders is seriously a tiresome task. A simple idea sparked in my mind to assign this tiresome task to the computer and this python program is 
an implementation of my idea.

This is an interactive python program which cleans the desktop (or preferrably any other directory) by moving the files of 
same type(extension) to a new directory or a directory that already exists. It also has various other functionalities.

The program gets the extension and the folder name as inputs and moves the files of that particular extension present 
in desktop into the folder specified by user.This program has been  developed using os,shutil,and re modules of python.
Upon initiating the program, it runs an infinite while loop where it asks for the inputs and finishes the job.

This program is implemented as a class DesktopInterface which has the following methods:

(i)__init__(desktop) - Constructor of the class which gets the path to desktop (or preferrably any other directory) as input and stores the files 
in the directory 

(ii)show_files(ext) - Prints all the files of the particular extension present in desktop

(iii)show_directories() - Prints all directories present in desktop

(iv)get_files_by__extension() - Returns the dictionary that contains all the files in desktop classified according to their extensions and prints the same

(v)classify(ext,dir) - Gets extension and directory as input and moves the files of that particular extension to the directory specified.
If the directory does not exist, the method creates a new directory.

(vi)delete_dir(dir) - Just an implementation of shutil.rmtree function which deletes a directory 
