from function import *

# Setup varibles: todo and done lists
todo = []
done = []

# Get system arguments
arg = sys.argv
rec = "-r" in arg
# move = "-m" in arg
log = "-l" in arg
src = isValidDir(arg[-2])
dst = isValidDir(arg[-1])

# Intro
print("\n")
print("-FiLLS STARTED-")
print("\n")
print("Opened path:", src)

# Sorting start
todo = sorting(src, dst, rec, move, log, todo, done)

# Add completed directory to done list
done.append(src)

# Run sorting into child directories if recursive option is True
if rec == True:
	for src in todo:
		if src not in done:
			if (log == True):
				print("Opened path:", src)
			todo = sorting(src, dst, rec, move, log, todo, done)
			done.append(src)

# Outro
print("\n")
print("Items have been sorted into:", dst)
print("\n")
print("-FiLLS FINISHED-")
exit()
