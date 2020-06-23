### 兼容系统 
- Linux 
- Mac OS

### Text2docx & Text2pdf & Docx2pdf 
[[English](./README.md)] 转换当前目录下指定文件或所有文件为 docx 或 pdf 格式。所有代码在program目录，测试文件在docs目录。

### 依赖 
	python3
	python-docx   
	$sudo pip3 install python-docx

### 使用 
    $ python3 Text2docx.py test.txt 
    $ python3 Text2pdf.py  test.txt
    $ python3 Docx2pdf.py  test.docx
    $ python3 Text2docx.py -a #-a 就是 --all 这将会转换所有txt为docx文件
    $ python3 Text2pdf.py  -a #转换当前目录所有txt为pdf
    $ python3 Docx2pdf.py  -a #转换当前目录所有docx为pdf

### 更好的用法
你可以将其加入系统中，当成系统指令来调用。具体操作如下：
	
	$ mv Text2docx.py Text2docx
	$ mv Text2pdf.py  Text2pdf 
	$ mv Docx2pdf.py  Docx2pdf 
	$ sudo chmod 755  Text2docx Text2pdf Docx2pdf
	$ sudo chown root Text2docx Text2pdf Docx2pdf
	$ sudo chgrp root Text2docx Text2pdf Docx2pdf
	$ sudo mv Text2docx /usr/bin/ #并不限于放到/usr/bin，也可以是/usr/local/bin
	$ sudo mv Text2pdf  /usr/bin/ #或者你随意创建个位置如/usr/local/shibin/
	$ sudo mv Docx2pdf  /usr/bin/ #然后在~/.vimrc中把/usr/local/shibin加入环境变量

就像使用系统指令一样，进入docs，目录下有一个test.txt

	$ cd docs
	$ ls
	-rw-r--r-- 1 shieber shieber  63 Jun 24 18:50 test.txt
	$ Text2docx test.txt 
	$ ls
	-rw-r--r-- 1 shieber shieber 36K Jun 24 19:45 test.docx
	-rw-r--r-- 1 shieber shieber  63 Jun 24 18:50 test.txt
	$ Docx2pdf  test.docx
	$ ls
	-rw-r--r-- 1 shieber shieber  36K Jun 24 19:46 test.docx
	-rw-r--r-- 1 shieber shieber 9.6K Jun 24 19:46 test.pdf
	-rw-r--r-- 1 shieber shieber   63 Jun 24 18:50 test.txt
	$ rm test.docx test.pdf
	$ ls
	-rw-r--r-- 1 shieber shieber   63 Jun 24 18:50 test.txt
	$ Text2pdf test.txt #还是会生成test.docx，然后生成test.pdf
	$ ls
	-rw-r--r-- 1 shieber shieber  36K Jun 24 19:46 test.docx
	-rw-r--r-- 1 shieber shieber 9.6K Jun 24 19:47 test.pdf
	-rw-r--r-- 1 shieber shieber   63 Jun 24 18:50 test.txt
