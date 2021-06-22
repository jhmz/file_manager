from os import rename, listdir

#path='F:\\example.txt'; extension = '.exe'; name = 'test'
def rename_files(path, extension, name):
    try:
        folder = listdir(path)
        count = 0

        for i in folder:
            if(extension in i):
                old = path + '\\{}'.format(i)
                new = path + '\\{}{}{}'.format(name,count,extension)
                rename(old,new)
                count = count + 1

    except:
        print('Invalid path or extension')
