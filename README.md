### Compatible OS 
- Linux 

### Text2docx & Docx2pdf & Text2pdf 
[[中文版](./README_CN.md)] Command line interface for converting txt file to docx, pdf file, convering docx file to pdf file. All codes in program and test file in docs.

### Requirement 
	python3 and python-docx   
	$sudo pip3 install python-docx

### Usage 
    $ python3 Text2docx.py test.txt 
    $ python3 Text2pdf.py  test.txt
    $ python3 Docx2pdf.py  test.docx
    $ python3 Text2docx.py -a #(-a equals --all will transfer all files)
    $ python3 Text2pdf.py  -a 
    $ python3 Docx2pdf.py  -a 

### Note 
You can add Text2docx.py and Docx2pdf.py into your OS as below. 
	
	$ mv Text2docx.py Text2docx
	$ mv Text2pdf.py  Text2pdf 
	$ mv Docx2pdf.py  Docx2pdf 
	$ sudo chmod 755  Text2docx Text2pdf Docx2pdf
	$ sudo chown root Text2docx Text2pdf Docx2pdf
	$ sudo chgrp root Text2docx Text2pdf Docx2pdf
	$ sudo mv Text2docx /usr/bin/ #not confined to /usr/bin/ 
	$ sudo mv Text2pdf  /usr/bin/ #you can also mv them into /usr/local/bin/
	$ sudo mv Docx2pdf  /usr/bin/ #or anywhere you like and then add it into PATH

Then you can use them  as system cmd: 

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
	$ Text2pdf test.txt 
	$ ls
	-rw-r--r-- 1 shieber shieber  36K Jun 24 19:46 test.docx
	-rw-r--r-- 1 shieber shieber 9.6K Jun 24 19:47 test.pdf
	-rw-r--r-- 1 shieber shieber   63 Jun 24 18:50 test.txt
