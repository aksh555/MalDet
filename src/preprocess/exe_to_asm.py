import os
import sys
import argparse
import shutil

parser = argparse.ArgumentParser(
    description='Use objdump to scan specfied folder for .exe files and dissamble them, i.e. convert to .asm files.')
parser.add_argument('-d', '--directory',
                    help='Location of Folder to scan for .exe files Ex. /home/user/malwares/EXE', required=True)
args = vars(parser.parse_args())

folderLoc = args['directory']

if not os.path.exists(folderLoc):
    print("Directory doesn't exist")
    sys.exit()


folderLoc2 = folderLoc+'/objdump_error'
if not os.path.exists(folderLoc2):
    os.system("mkdir \"" + folderLoc2+"\"")

folderLoc3 = folderLoc+'/assembly_codes'
if not os.path.exists(folderLoc3):
    os.system("mkdir \"" + folderLoc3+"\"")

files = []
for file in os.listdir(folderLoc):
    if file.endswith(".exe"):
        files.append(file)
    if file.endswith(".EXE"):
        files.append(file)

total_count = len(files)
error_count = 0
print(f"Total files: {total_count}")

for file in files:
    source = folderLoc+'/'+file
    dest = folderLoc3+'/'+file
    test = "objdump -d \"" + source + "\" 2> error_file > \"" + dest + ".asm\""
    os.system(test)

    f1 = open('error_file', 'rb')
    a = f1.readline()
    if a:
        b = a.split()
        if b[0] == "objdump:":
            tempfile1 = dest+".asm"
            os.remove(tempfile1)
            error_count += 1
            destination = folderLoc2+'/'
            shutil.move(source, destination)
    f1.close()

print(f"Error files: {error_count}")
