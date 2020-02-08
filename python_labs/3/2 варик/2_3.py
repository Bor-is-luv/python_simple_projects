import os

files = os.listdir(path=".")
py_files = [os.path.abspath(file) for file in files if os.path.getsize(file) < 1024*1024 and os.path.isfile(file)]
dir = [os.path.abspath(file) for file in files if os.path.isdir(file)]
for folder in dir:
    os.chdir(folder)
    files = os.listdir(path=".")
    for file in files:
        if os.path.getsize(file) < 1024*1024 and os.path.isfile(file):
            py_files.append(os.path.abspath(file))
        elif os.path.isdir(file):
            dir.append(os.path.abspath(file))

print(py_files)