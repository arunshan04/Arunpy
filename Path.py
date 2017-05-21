import os
print ('myjob')

mypath='/home/arun'
for i in dir():
    print (i)

def getpath(mypath):
    if os.path.exists(mypath):
        return ([os.path.join(mypath,fn) for fn in next(os.walk(mypath))[2]])
    else:
        return ''




print (os.listdir(mypath))
mypath='/home/hduser/../'
for i in getpath(mypath):
    print (i)