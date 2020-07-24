#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Shieber
# Date: 2019.07.24
# Modified: 2020.07.24

import sys
import time
from os.path import basename 
from subprocess import call

def trans2pdf():
    argv = sys.argv
    if len(sys.argv) < 2:
        program = basename(argv[0])
        print(f"Usage: {program} test.txt or {program} -a"%(program,program))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        fils = listdir('.')
    else:
        fils = argv[1:]

    for fl in fils:
        if fl.endswith('.txt'):
            call(f'Text2docx {fl} >/dev/null', shell=True)
            call(f'Docx2pdf {''.join([fl.split('.')[0],'.docx'])}%s >/dev/null', shell=True)

if __name__ == '__main__':
    start = time.time()
    trans2pdf()
    end = time.time()
    print(f'耗时：{end - start:.2f}(s)')
