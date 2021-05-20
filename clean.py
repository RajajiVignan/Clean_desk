import glob, os, shutil
from pathlib import Path

source_dir = "C:\\Users\\PC\\Desktop\\test_python"

dest_dir = "C:\\Users\\PC\\Desktop\\test_python\\New folder2"
files = glob.iglob(os.path.join(source_dir, "*.exe"))
print(files)
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dest_dir)


dest_dir2 = os.path.join(source_dir, "Image_files")
#"C:\\Users\\PC\\Desktop\\test_python\\New folder3"
bigfiles = []
files2 = glob.iglob(os.path.join(source_dir, "*.png"))
files3 = glob.iglob(os.path.join(source_dir, "*.jpg"))
#bigfiles.append(files2)
files = ["*.png", "*.jpg"]
paths = glob.iglob(os.path.join(source_dir, f) for f in files)

print(paths)
print(files3)

for file in paths:
    if os.path.isfile(file):
        if os.path.exists(dest_dir2) == True:
            shutil.move(file, dest_dir2)
        else:
            os.mkdir(dest_dir2)
            shutil.move(file,dest_dir2)



#filename = Path(source_dir/ '*.txt')
