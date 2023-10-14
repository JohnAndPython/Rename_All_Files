#########################################################################################
# Rename files to this format: filename_nnnn.extension | n = digit | nnnn starts at 0001
# The extension remains the same
# The filname can be changed as wished: variable newprefix
#########################################################################################

import os

if __name__ == "__main__":
    #enter the folder path, in which you want to changes the file names
    path = "Directory Path" #For Example: C:\\Users\\name\\Documents

    if not os.path.exists(path):
        raise NotADirectoryError("Directory does not exist")

    files = os.listdir(path)

    #new filename prefix
    newprefix = "NEW_FILENAME_"
    last_number = 0

    #get missing numbers in filenames that start with newprefix
    missingnumbers = list()
    all_numbers_fromfile = [int(nf_file.split(".")[0].split("_")[-1]) for nf_file in files if nf_file.startswith(newprefix)]
    if all_numbers_fromfile:
        first_number = all_numbers_fromfile[0]
        last_number = all_numbers_fromfile[-1]

        missingnumbers = (number for number in range(first_number, last_number + 1) if number not in all_numbers_fromfile)

    #get all files without newprefix
    notnffiles = (notnf_file for notnf_file in files if not notnf_file.startswith(newprefix))

    #if there are files with newprefix but missing numbers: rename files without newprefix
    for number in missingnumbers:
        for notnf_file in notnffiles:
            file_suffix = os.path.splitext(notnf_file)[1]

            old_file_name = path + f"\\{notnf_file}"
            new_file_name = path + (f"\\{newprefix}" + f"{number}".zfill(4) + file_suffix)

            if not os.path.isfile(new_file_name):
                os.rename(old_file_name, new_file_name)
            break

    #rename all missing files without newprefix
    for notnf_file in notnffiles:
        last_number += 1
        file_suffix = os.path.splitext(notnf_file)[1]

        old_file_name = path + f"\\{notnf_file}"
        new_file_name = path + (f"\\{newprefix}" + f"{last_number}".zfill(4) + file_suffix)

        if not os.path.isfile(new_file_name):
            os.rename(old_file_name, new_file_name)
