import subprocess

#subprocess.call('ls -lrt', shell=True)

def execute(command):
    for i in command.split('|'):
        ps1=subprocess.Popen([i],stdout=subprocess.PIPE)
        print ps1.communicate()[0]



execute('ps')


import os

print os.chdir()