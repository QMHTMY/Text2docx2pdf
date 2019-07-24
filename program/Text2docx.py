#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2019 Shieber
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
# 将txt文件转换为docx文档
# -a 将当前目录所有txt文件转换为docx格式

import re, sys,time
from os import listdir
from docx import Document 
from os.path import exists, basename 

def getTitle(filename):
    '''获取txt和title'''
    try:
        txtobj = open(filename)
        title  = txtobj.readline() #.decode('utf-8')
        text   = txtobj.read() #.decode('utf-8')     #decode还原为utf-8  encode
        txtobj.close() 
    except Exception as err:
        print("Error, file does not exist")
        txtobj.close() 
        sys.exit(-1)

    return title, text

def write2docx(docxname,title,text):
    '''将text内容写入docx'''
    if not text:
        print("Erro,no texture")
        sys.exit(-1)

    if exists(docxname):
        docx = Document(docxname)
    else:
        docx = Document()

    try:
        docx.add_heading(title)
        docx.add_paragraph(text)
    except Exception as err:
        print("错误:%s"%err)
        sys.exit(-1)

    docx.save(docxname)

def transfer(fil):
    docxname   = ''.join([fil.split('.')[0],'.docx'])
    title,text = getTitle(fil)
    write2docx(docxname,title,text)

def text2docx():
    '''主函数'''
    argv = sys.argv
    if len(argv) < 2:
        program = basename(argv[0])
        print("Usage: %s [s1.txt] or %s -a"%(program,program))
        sys.exit(-1)

    if '-a' == argv[1] or '--all' == argv[1]:
        for fil in listdir('.'):
            if not fil.endswith('.txt'):
                continue
            transfer(fil)
    else:
        for fil in argv[1:]:
            if not fil.endswith('.txt'):
                continue
            transfer(fil)

if __name__ == "__main__":
    start = time.time()
    text2docx()
    end  = time.time()
    print('耗时：%.2f(s)'%(end - start))
