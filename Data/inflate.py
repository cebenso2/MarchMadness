import os
import sys
DATA_LOCATION = "FullData"

if not os.path.exists(DATA_LOCATION):
    os.makedirs(DATA_LOCATION)
else:
    print("Data directory already exists. Remove this folder")
    sys.exit(0)
os.chdir(DATA_LOCATION)

COMPRESSED_DATA_LOCATION = "../CompressedData"
files = os.listdir(COMPRESSED_DATA_LOCATION)
for f in files:
    dir = f[:-4]
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.system("cp " + COMPRESSED_DATA_LOCATION + "/" + f + " " + dir)
    os.chdir(dir)
    os.system("unzip *")
    os.system("rm *.zip")
    os.chdir("..")
    
