------------------------------------
 # Text2docx & Docx2pdf & Text2pdf #
------------------------------------
<li><a href="README_CN.md">中文版</a></li>
<li> Command line interface for converting txt file to docx, pdf file, convering docx file to pdf file.</li>
<li> All codes in program and test file in docs</li>

# Requirement #
<li> python3 </li>
<li> python-docx </li>
$sudo pip3 install python-docx

# Usage #
    $ python3 Text2docx.py test.txt 
    $ python3 Text2pdf.py  test.txt
    $ python3 Docx2pdf.py  test.docx
    $ python3 Text2docx.py -a (-a equals --all) (transfer all files)
    $ python3 Text2pdf.py  -a 
    $ python3 Docx2pdf.py  -a 

# Note #
You can add Text2docx.py and Docx2pdf.py into your OS as below. 
	
	$ mv Text2docx.py Text2docx
	$ mv Text2pdf.py  Text2pdf 
	$ mv Docx2pdf.py  Docx2pdf 
	$ sudo chmod 755  Text2docx, Text2pdf, Docx2pdf
	$ sudo chown root Text2docx, Text2pdf, Docx2pdf
	$ sudo chgrp root Text2docx, Text2pdf, Docx2pdf
	$ sudo mv Text2docx /usr/bin/
	$ sudo mv Text2pdf  /usr/bin/
	$ sudo mv Docx2pdf  /usr/bin/

Then you can use them  as system orders: 

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
