# FiLLS
Python script to sort images

FiLLS v0.1
## Summary
- Search through 'Source' folder (Recursive optional)
- Find images with specified 'Extentions' (jpg, jpeg, tiff, raw)
- Read images 'Meta-data' for 'Sorting' ('exifread' package required)
- 'Copy' or 'Move' (Move not yet available) files to 'Destination' folder

## Arguments:
* Required - Source and Destination as second and last arguments
example: python3 fills.py -r /Volumes/storage/source /Volumes/storage/destination
Optional - Enter after script name in terminal python3 fills.py -args
-r = Recursive (Default will only search items within source folder skipping sub folders)
-m = Move (Default will copy the file) - not yet available
-l = Log to terminal (Default will not log actions to terminal)
