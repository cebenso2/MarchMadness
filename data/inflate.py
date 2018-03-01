import os
import sys
DATA_LOCATION = "full"

if not os.path.exists(DATA_LOCATION):
    os.makedirs(DATA_LOCATION)
else:
    print("Data directory already exists")
    sys.exit(0)
os.chdir(DATA_LOCATION)

COMPRESSED_DATA_LOCATION = "../compressed"
files = os.listdir(COMPRESSED_DATA_LOCATION)
for f in files:
    dir = f[:-4]
    if "Play" in dir:
        dir = "PlayByPlay"
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.system("cp " + COMPRESSED_DATA_LOCATION + "/" + f + " " + dir)
    os.chdir(dir)
    os.system("unzip " + f)
    os.system("rm *.zip")
    os.chdir("..")
    
