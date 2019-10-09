-----------
# 兼容系统 #
------------
	Unix-like OS

------------------------------------
 # Text2docx & Text2pdf & Docx2pdf #
------------------------------------
<li><a href="README.md">English</a></li>
<li> 转换当前目录下制定文件或所有文件为 docx 或 pdf 格式。</li>
<li> 所有代码在program目录，测试文件在docs目录</li>

# 依赖 #
<li> python3 </li>
<li> python-docx </li>
$sudo pip3 install python-docx

# 使用 #
    $ python3 Text2docx.py test.txt 
    $ python3 Text2pdf.py  test.txt
    $ python3 Docx2pdf.py  test.docx
    $ python3 Text2docx.py -a (-a equals --all) (transfer all files)
    $ python3 Text2pdf.py  -a 
    $ python3 Docx2pdf.py  -a 

# 注意 #
你可以将其加入系统中，当成系统指令来调用。具体操作如下：
	
	$ mv Text2docx.py Text2docx
	$ mv Text2pdf.py  Text2pdf 
	$ mv Docx2pdf.py  Docx2pdf 
	$ sudo chmod 755  Text2docx, Text2pdf, Docx2pdf
	$ sudo chown root Text2docx, Text2pdf, Docx2pdf
	$ sudo chgrp root Text2docx, Text2pdf, Docx2pdf
	$ sudo mv Text2docx /usr/bin/
	$ sudo mv Text2pdf  /usr/bin/
	$ sudo mv Docx2pdf  /usr/bin/

就像使用系统指令一样，假如docs目录下有一个test.txt

	$ cd docs
	$ ls
	-rw-r--r-- 1 shieber shieber  63 Jun 24 18:50 test.txt
	$ Text2docx test.txt 
	$ ls
	-rw-r--r-- 1 shieber shieber 36K Jun 24 19:45 test.docx
	-rw-r--r-- 1 shieber shieber  63 Jun 24 18:50 test.txt
	$ Text2pdf test.txt 
	$ ls
	-rw-r--r-- 1 shieber shieber  36K Jun 24 19:46 test.docx
	-rw-r--r-- 1 shieber shieber 9.6K Jun 24 19:46 test.pdf
	-rw-r--r-- 1 shieber shieber   63 Jun 24 18:50 test.txt
	$ Docx2pdf  test.docx
	$ ls
	-rw-r--r-- 1 shieber shieber  36K Jun 24 19:46 test.docx
	-rw-r--r-- 1 shieber shieber 9.6K Jun 24 19:47 test.pdf
	-rw-r--r-- 1 shieber shieber   63 Jun 24 18:50 test.txt
