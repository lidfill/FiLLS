###
#
#	FiLLS v0.1
#
###
#	Summary
###
#
#	- Search through 'Source' folder (Recursive optional)
#	- Find files with specified 'Extentions' (jpg, jpeg, png)
#	- Read file 'Meta-data' for 'Sorting'
#	- 'Copy' or 'Move' files to 'Destination' folder
#
#	Arguments:
#		* Required - Source and Destination as second and last arguments
#			example: python3 fills.py -r /Volumes/storage/source /Volumes/storage/destination
#		Optional - Enter after script name in terminal python3 fills.py -args
#			-r = Recursive (Default will only search within source folder)
#			-l = Log to terminal (Default will not log actions to terminal)
###
from function import *

arg = sys.argv

rec = "-r" in arg
log = "-l" in arg

try:
	if checkDir(arg[-2]):
		src = arg[-2]
	else:
		print("Source directory error")
		exit()
except:
	print("Missing required arguments, make sure to include source and destination.")
	exit()

try:
	if checkDir(arg[-1]):
		dst = arg[-1]
	else:
		print("Destination directory error")
		exit()
except:
	print("Missing required arguments, make sure to include source and destination.")
	exit()

