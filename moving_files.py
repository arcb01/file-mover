import os
import ctypes, sys
from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil


def read_directory(path):
    if len(listdir(path)) != 0:
        return listdir(path) 


def make_folders(destination):
    if os.path.isdir(source) and os.path.isdir(destination):
        # Creating storing folders
        if not (os.path.isdir(destination + "\\" + "jpg-photos") and \
        os.path.isdir(destination + "\\" + "raw-photos")):
            os.mkdir(destination + "\\" + "jpg-photos")
            os.mkdir(destination + "\\" + "raw-photos")


def main_copy(source, destination):
    
    make_folders(destination)
    

    # List of all files inside directory
    files_fullpath = [f for f in listdir(source) 
                        if isfile(join(source, f))] 

    # Copy files to the correct folder according to filetype
    if len(files_fullpath) != 0:
        for fs in files_fullpath:
            full_file = source + "\\" + fs
            if str(fs).endswith('.ARW'):
                shutil.copy(full_file, raw_folder + "\\" + fs)
            else:
                shutil.copy(full_file, jpg_folder + "\\" + fs)
        if len(listdir(destination)) != 0:
            print("Files moved succesfully!")


# When files are removed from one folder, they should be also 
# removed from the other folder (both ways).


def remove(jpg_folder, raw_folder):
    # List files from both directories, compare them and only 
    # keep the ones that are repeated

    jpg_files = read_directory(jpg_folder)
    raw_files = read_directory(raw_folder)

    filenames_to_keep = list( map(lambda el : el.split(".")[0], jpg_files) )
    #files_to_remove = list(set(raw_files) ^ set(files_to_keep))

    # Changing .JPG to .ARW
    #filenames_to_remove = list( map(lambda el : el.split(".")[0] + ".ARW", files_to_remove) )

    for f in raw_files:
        filename = f.split(".")[0]
        if filename not in filenames_to_keep:
            path = raw_folder + "\\" + filename + ".ARW"
            os.remove(path)


if __name__ == "__main__":

    # Enter source and destionation directories
    source = input("\nEnter source folder where files are: ")
    destination = input("Enter destination folder where files will be copied to: ")

    # Folders created 
    jpg_folder = destination + "\\" + "jpg-photos"
    raw_folder = destination + "\\" + "raw-photos"

    main_copy(source, destination)

    i = input("\nDo you want to REMOVE some files? [Y/N] ")

    if i == "Y" or i == "y":
        print("Time to remove some files!!!!\n")
        blank = input("Press ENTER when you've removed some files from jpg-folder: ")

        if blank == "":
            remove(jpg_folder, raw_folder)
