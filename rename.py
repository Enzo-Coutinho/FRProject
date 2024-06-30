import os
path = 'images/train/tired'
files = os.listdir(path)
print(len(files))
print(files)
def rename():
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+35886), '.jpg'])))

for index, file in enumerate(files, start=0):
        print(index)
        if index == 500:
           break
        else:
            os.remove(os.path.join(path, files[index]))
