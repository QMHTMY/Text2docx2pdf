#!/usr/bin/python3
# -*- coding: utf-8 -*-

#    Author: Shieber
#    Date: 2019.07.24
#
#                             APACHE LICENSE
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
#                            Function Description
#    transfer txt file to pdf file.
#    -a option means transfer all txt files in the current directory to pdf.
#
#    Copyright 2019 
#    All Rights Reserved!

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
