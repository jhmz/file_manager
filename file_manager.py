import os
from shutil import move

#this function will rename every file with the extension in the path to the name passed as paramter followed by a count;
#this parameters (path='F:\\example', extension = '.png', name = 'test') would result in:
#test1.png;test2.png;test3.png;test4.png;test5.png...
def rename_files(path, extension, name):
    folder = os.listdir(path)
    count = 0

    for i in folder:
        if(extension in i):
            old = path + '\\{}'.format(i)
            new = path + '\\{}{}{}'.format(name,count,extension)
            os.rename(old,new)
            count = count + 1

#this function organize the files in folders separated by extension;
#example: if there's files .png and .mp4 in a folder it will create a folder for .png files and a folder for .mp4 files and move them respectively.
def organize_extensions(path):
    folder = os.listdir(path)
    files = []
    extensions = []
    #getting files and extensions path
    for file in folder:
        filename, extension = os.path.splitext(file)
        files.append(file)
        if(extension.lower() not in extensions):
            extensions.append(extension.lower())

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
                    move(path+'\\'+file,path+'\\'+extension.lower()+'\\'+file)
