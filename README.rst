Text2docx
=============
Command line interface for converting txt file to docx file

Versions
--------
Text2docx works only with Python 3

Requirement
------------
python-docx 

::

    $ sudo pip3 install python-docx

Usage
-----

::

    $ Text2docx [s1.txt] or Text2docx -a  
    $ Text2docx -a  


Details
--------
"-a" option is to convert every txt file in current directory to docx.
Please add the Text2docx into /usr/bin  and change its mode.

mv Text2docx Text2docx

sudo chmod 755 Text2docx

sudo chown root Text2docx

sudo chgrp root Text2docx

sudo mv Text2docx /usr/bin
