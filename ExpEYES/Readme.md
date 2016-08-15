ExpEYES Software

Full software documentation at http://www.expeyes.in/software.html
Github Repository: https://github.com/expeyes/expeyes-programs

ExpEYES software is written in Python and it should run on any computer having Python interpreter (version > 2.7) and Python Serial library. It is included in the Debian and Ubuntu (version > 13.04) GNU/Linux distributions. Otherwise it can be installed from expeyes.deb file.
For Ubuntu versions 10.04 to 12.10 you may use this deb file.

1. The expEYES Live ISO images for DVDs and USB pendrives

The fastest way to get expEYES running on your PC is to boot your computer from a DVD or USB pendrive, prepared using the ISO image. The procedure to to this on MSWindows is explained here. Once you boot from the pen-drive, the Lubuntu desktop will appear. Start the expEYES program from the Applications->Science menu. Download the ISO images of the Live DVD. This ISO image is prepared from Lubuntu 14.04 and contains other educational resources also.

3. On Other GNU/Linux Distributions

Download expeyes.zip and do the following:

$unzip expeyes.zip

$ cd eyes-junior

$ sudo python croplus.py

To use the device as a normal user, download the file to set the USB permissions by running.

# sh postinst.sh

4. On MS Windows

Since the programs are written in Python, the same source code works on GNU/Linux and Windows. You need to install Python Interpreter and the required libraries. The USB device appears as an RS232 connection to the software. The virtual COM port is established by the driver software for the USB to Serial converter MCP2200

You need to install

MCP2200 Driver
Python Interpreter version 2.7xx
Python Serial module
Python TkInter module
Python Imaging Library module
Scipy and Numpy modules
Then run the program croplus.py

Windows version of the program
A native Windows program is also available. It includes the main osciloscope application and severel experiments. More details are at http://www.expeyes.herobo.com/
