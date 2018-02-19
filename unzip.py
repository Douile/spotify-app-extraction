import os
import os.path
import zipfile

def extractzip(name):
    file = os.path.join(datafolder,name)
    if zipfile.is_zipfile(file):
        output = os.path.join(outputfolder,name)
        with zipfile.ZipFile(file,"r") as zip:
            zip.extractall(output)
        print("Extracted %s" % (name))

cdir = os.getcwd()
datafolder = os.path.join(cdir,"data/")
outputfolder = os.path.join(cdir,"output/")

for dir, dirname, files in os.walk(datafolder):
    for file in files:
        extractzip(file)
