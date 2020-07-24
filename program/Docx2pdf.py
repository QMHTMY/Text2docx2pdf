#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Shieber
# Date: 2019.07.24
# Modified: 2020.07.24

import sys,time
from os.path import  basename 
from subprocess import call

def trans2pdf():
    argv = sys.argv
    if len(sys.argv) < 2:
        script = basename(argv[0])
        print(f'Usage: {script} name.docx or {script} -a')
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        order = 'libreoffice --invisible --convert-to pdf *.docx 1>/dev/null 2>&1'
    else:
        if argv[1].endswith('.docx'):
            order = 'libreoffice --invisible --convert-to pdf {argv[1]} 1>/dev/null 2>&1'
        else:
            print('Error, file type does not match!')
            sys.exit(-1)

    call(order,shell=True)

if __name__ == '__main__':
    start = time.time()
    trans2pdf()
    end = time.time()
    print(f'耗时：{end - start:.2f}(s)')
