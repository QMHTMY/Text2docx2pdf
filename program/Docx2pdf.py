#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
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
#    transfer docx file to pdf file.
#    -a option means transfer all docx files in the current directory to pdf.
#
#    Copyright 2019 
#    All Rights Reserved!

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
