import os
import sys
import argparse

'''
opcodeList.txt contains the list of opcodes that we have to scan.
We save all the opcodes in a list.
'''

f1 = open('opcodeList.txt', 'r')
opcodes = []
opcodes.append('FileName')
for eachLine in f1:
    opcodes.extend(eachLine.split())
f1.close()

num_opcodes = len(opcodes)-1


# Argument Parser
parser = argparse.ArgumentParser(
    description='Output a csv file containing the frequency of all opcodes for each .asm file in the specified directory.')
parser.add_argument('-d', '--directory',
                    help='Location of Directory(folder) to scan for .asm files', required=True)
parser.add_argument('-o', '--outfile',
                    help='Name of the output .csv file', required=True)
args = vars(parser.parse_args())

folderLoc = args['directory']
out_file = args['outfile']

# Checking if the user entered directory exists or not.
if not os.path.exists(folderLoc):
    print("Directory doesn't exist")
    sys.exit()

'''
Scanning the entered folder for .ASM files and 
adding their names in a list
'''

files = []
for file in os.listdir(folderLoc):
    if file.endswith(".ASM"):
        files.append(file)
    if file.endswith(".asm"):
        files.append(file)


# Checking if the folder contains no .ASM files.
if len(files) == 0:
    print("No .ASM or .asm files exist in folder specified")
    sys.exit()

# Output file
outfile = open('%s' % out_file, 'w')


firstLine = []
firstLine.append('FileName')
for i in range(1, num_opcodes+1):
    firstLine.append(i)
outfile.write(",".join(str(x) for x in firstLine))
outfile.write("\n")


print(f"Converting {len(files)} files")
for file in files:
    f1 = open(os.path.join(folderLoc, file), 'r', encoding="latin-1")
    number = [0]*(num_opcodes+1)
    fl = file.split(".")
    filename = ".".join(fl[:-2])
    print(filename)
    number[0] = '%s' % filename
    if os.stat(os.path.join(folderLoc, file)).st_size != 0:
        for line in f1:
            splitter = line.split()
            if splitter:
                for x in splitter:
                    if not(x[0] == ';') and x[0].isalpha():
                        if x in opcodes:
                            number[opcodes.index(x)] += 1
    outfile.write(",".join(str(x) for x in number))
    outfile.write("\n")
    f1.close()

outfile.close()
