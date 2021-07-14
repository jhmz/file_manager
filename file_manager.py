import os
from shutil import move
#path='F:\\example.txt'; extension = '.exe'; name = 'test'
def rename_files(path, extension, name):
    try:
        folder = os.listdir(path)
        count = 0

        for i in folder:
            if(extension in i):
                old = path + '\\{}'.format(i)
                new = path + '\\{}{}{}'.format(name,count,extension)
                os.rename(old,new)
                count = count + 1

    except:
        print('Invalid path or extension')

#function that organizes the files in folders separated by extension
def organize_extensions(path):
    try:
        folder = os.listdir(path)
        files = []
        extensions = []
        #getting files and extensions path
        for file in folder:
            filename, extension = os.path.splitext(file)
            files.append(file)
            if(extension not in extensions):
                extensions.append(extension)

        for i in range(len(extensions)):
            if(extensions[i] == 'ini'):
                extensions.pop(i)
            elif(extensions[i]== ''):
                extensions.pop(i)

            #creating folders for extensions
        for extension in extensions:
            os.mkdir(path+'\\'+extension)
            #moving files to each extension folder
        for file in files:
            for extension in extensions:
                if(extension in file):
                    move(path+'\\'+file,path+'\\'+extension+'\\'+file)
                    
    except:
        print('Invalid path or extension')
