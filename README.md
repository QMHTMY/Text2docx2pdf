-----------------------
 # Text2docx & Docx2pdf #
-----------------------
Command line interface for converting txt file to docx file, docx file to pdf file.

# Requirement #
<li> python3 </li>
<li> python-docx </li>
$sudo pip3 install python-docx

# Usage #
    $ python3 Text2docx.py name.txt 
    $ python3 Text2docx.py -a (-a equals --all) (transfer all txt in the current dir to docx)
    $ python3 Docx2pdf.py name.docx
    $ python3 Docx2pdf.py -a  (-a equals --all) (transfer all docx in the current dir to pdf)

# Note #
You can add Text2docx.py and Docx2pdf.py into your OS as below. 
	
	$ mv Text2docx.py Text2docx
	$ mv Docx2pdf.py  Docx2pdf 
	$ sudo chmod 755 Text2docx, Docx2pdf
	$ sudo chown root Text2docx, Docx2pdf
	$ sudo chgrp root Text2docx, Docx2pdf
	$ sudo mv Text2docx /usr/bin/
	$ sudo mv Docx2pdf  /usr/bin/

Then you can use them  as system orders: 

	$ ls
	-rw-r--r-- username grpname 3.5M Jun 24 15:27 name.txt
	$ Text2docx -a
	$ Text2docx name.txt 
	$ Docx2pdf -a
	$ Docx2pdf name.docx

Find your files on the current directory:
	
	$ ls
	-rw-r--r-- username grpname 2.1M Jun 24 15:28 name.docx
	-rw-r--r-- username grpname 2.0M Jun 24 15:28 name.pdf
	-rw-r--r-- username grpname 1.0M Jun 24 15:27 name.txt
