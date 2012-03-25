#!/usr/bin/env python
#python3

## this script is quite old but still works on my system
## please report any problems if you face any problem
## Also note that his script is designed to work with Python 3

import os

def folder(a):
    '''extract folders from a list'''
    b=[]
    for i in a:
        if not i.__contains__('.'):
            b.append(i)
    return b

d={}
'''dictionary to store the folder tree'''

def path(pth):
    '''recursively call this func to
    generate the folder tree'''
    d.__setitem__(pth,os.listdir(pth))
    b=folder(d[pth])
    for i in b:
        try:
            path(pth+"\\"+i)
        except WindowsError:
            continue

def show_dict():
    '''print the dictionary'''
    for i in d.keys():
        print(i)
        for j in d[i]:
            print('  '+j)

def print_dict():
    '''write the dictionary to a file'''
    f=open('directory.txt','w',encoding='utf-8')
    for i in d.keys():
        f.write(i+os.linesep)
        for j in d[i]:
            f.write('  '+j+os.linesep)
    f.close()

if __name__=='__main__':
    path(os.getcwd())
    x=input('Write to file(1) or print(2)?')
    if x=='1':
        print_dict()
    elif x=='2':
        show_dict()
    else:
        print('wrong input... exiting...')
