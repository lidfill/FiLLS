import sys
import os

def checkDir(folder):
	if os.path.isdir(folder):
		return(True)
	else:
		print("Path:", folder, "Invalid")
		return(False)
