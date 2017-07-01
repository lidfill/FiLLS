#!/usr/bin/python
import sys
import os
import time
import shutil
import exifread

# Supported file types which will be sorted
extentions = ['.jpg', '.jpeg', '.tiff', '.raw']

# Return a valid path
def recreatePath(path):
	tmppath = os.path.split(path)
	path = os.path.join(*tmppath)
	return(path)

# Check and return a valid path
def isValidDir(path):
	tmppath = os.path.split(path)
	path = os.path.join(*tmppath)
	if os.path.isdir(path):
		return(path)
	else:
		print("\n")
		print("Error at path:", path)
		exit()

# Basic validation on file, will not action items starting with '.' or '$'
def basicValidate(item):
	if (item[:1] == ".") or (item[:1] == "$"):
		return(False)
	return(True)

# Convert digital month to english name
def monthName(x):
	return {
		'01':'January',
		'02':'February',
		'03':'March',
		'04':'April',
		'05':'May',
		'06':'June',
		'07':'July',
		'08':'August',
		'09':'September',
		'10':'October',
		'11':'November',
		'12':'December',
	}[x]

# Try extract date from EXIF datetime into MM/DD/YYYY format
def exifCreatedDate(item, log):
	f = open(item, 'rb')
	tags = exifread.process_file(f)
	if 'EXIF DateTimeOriginal' in tags:
		exif = str(tags['EXIF DateTimeOriginal'])[0:10]
		exif = exif.split(":")
		if len(exif) == 3:
			exif = exif[1] + "/" + exif[2] + "/" + exif[0]
			return exif
		else:
			if log == True:
				print("File does not have EXIF Meta data to sort correctly, will sort based on files creation date")
			return(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(item))))
	elif 'EXIF DateTime' in tags:
		print('exif datetime')
		exif = str(tags['EXIF DateTime'])[0:10]
		exif = exif.split(":")
		if len(exif) == 3:
			exif = exif[1] + "/" + exif[2] + "/" + exif[0]
			return exif
		else:
			if log == True:
				print("File does not have EXIF Meta data to sort correctly, will sort based on files creation date")
			return(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(item))))
	else:
		if log == True:
			print("File does not have EXIF Meta data to sort correctly, will sort based on files creation date")
		return(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(item))))

# Copy file to destination
def copyFile(src, dst, this, log):
	if os.path.isfile(dst + os.sep + this) is not True:
		shutil.copy(src, dst)
		if (log == True):
			print("Copied:", src, "To:", dst)
	else:
		if (log == True):
			print(src, "already exists - Skipped")

# Find files in source folder and sort according to created time
def sorting(src, dst, rec, move, log, todo, done):
	for this in os.listdir(src):
		if os.path.isfile(recreatePath(src + os.sep + this)):
			if os.path.splitext(this)[1].strip().lower() in extentions:
				if basicValidate(this):
					if (log == True):
						print("Found an image:", this)
					# Read Exif meta data
					created = exifCreatedDate(src + os.sep + this, log)
					print(created)
					month = monthName(created[:2])
					year = created[-4:]
					tmpdst = dst + os.sep + year + os.sep + month
					# Sort item - Double take
					if os.path.isdir(dst + os.sep + year):
						if os.path.isdir(tmpdst):
							copyFile(recreatePath(src + os.sep + this), tmpdst, this, log)
						else:
							os.mkdir(tmpdst)
							copyFile(recreatePath(src + os.sep + this), tmpdst, this, log)
					else:
						os.mkdir(dst + os.sep + year)
						if os.path.isdir(tmpdst):
							copyFile(recreatePath(src + os.sep + this), tmpdst, this, log)
						else:
							os.mkdir(tmpdst)
							copyFile(recreatePath(src + os.sep + this), tmpdst, this, log)
		elif os.path.isdir(recreatePath(src + os.sep + this)):
			if (log == True):
				print("Found a folder:", this)
			if (rec == True):
				tmpsrc = recreatePath(src + os.sep + this)
				todo.append(tmpsrc)
	return(todo)
