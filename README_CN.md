-----------------------
 # Text2docx & Docx2pdf #
-----------------------
<li><a href="README.md">English</a></li>
<li> 转换当前目录下制定文件或所有文件为 docx 或 pdf 格式。</li>

# 依赖 #
<li> python3 </li>
<li> python-docx </li>
$sudo pip3 install python-docx

# 使用 #
    $ python3 Text2docx.py name.txt 
    $ python3 Docx2pdf.py  name.docx
    $ python3 Text2docx.py -a (-a 就是 --all) (转换当前目录下所有文件)
    $ python3 Docx2pdf.py  -a  

# 注意 #
你可以将其加入系统中，当成系统指令来调用。具体操作如下：
	
	$ mv Text2docx.py Text2docx
	$ mv Docx2pdf.py  Docx2pdf 
	$ sudo chmod 755  Text2docx, Docx2pdf
	$ sudo chown root Text2docx, Docx2pdf
	$ sudo chgrp root Text2docx, Docx2pdf
	$ sudo mv Text2docx /usr/bin/
	$ sudo mv Docx2pdf  /usr/bin/

就像使用系统指令一样，假如docs目录下有一个test.txt

	$ cd docs
	$ ls
	-rw-r--r-- 1 shieber shieber  63 Jun 24 19:51 test.txt
	$ Text2docx test.txt 
	$ ls
	-rw-r--r-- 1 shieber shieber 36K Jun 24 19:51 test.docx
	-rw-r--r-- 1 shieber shieber  63 Jun 24 19:51 test.txt
	$ Docx2pdf  test.docx
	$ ls
	-rw-r--r-- 1 shieber shieber  36K Jun 24 19:51 test.docx
	-rw-r--r-- 1 shieber shieber 9.6K Jun 24 19:52 test.pdf
	-rw-r--r-- 1 shieber shieber   63 Jun 24 19:51 test.txt
