#!/usr/bin/python3
# coding: utf-8
# Author: Shieber
# Date: 2019.07.24
# transfer docx to pdf
# -a option means transfer all docx files in the current directory to pdf type.
#

import sys,time
from os.path import  basename 
from subprocess import call

def transfer(fils):
    for fil in fils:
        if fil.endswith('.txt'):
            call('Text2docx %s >/dev/null '%fil, shell=True)
            call('Docx2pdf %s >/dev/null'%(''.join([fil.split('.')[0],'.docx'])),shell=True)

def trans2pdf():
    argv = sys.argv
    if len(sys.argv) < 2:
        program = basename(argv[0])
        print("Usage: %s test.txt or %s -a"%(program,program))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        fils = listdir('.')
    else:
        fils = argv[1:]

    transfer(fils)

if __name__ == '__main__':
    start = time.time()
    trans2pdf()
    end = time.time()
    print('耗时：%.2f(s)'%(end - start))
