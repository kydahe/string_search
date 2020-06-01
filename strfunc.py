import os
import sys

filelists = []

def get_files(file_dir):
    for filepath, dirnames, filenames in os.walk(file_dir):
	return filenames, dirnames, filepath

def findstring(pathfile):
    fp = open(pathfile, "r+")
    #strr = fp.read()
    a = 0
    ret = 0
    #print ""
    #for (num, value) in enumerate(pathfile):
    for line in fp.readlines():
	a = a+1
	#if(value.find("encrypt")!=-1):
	if "strcat" in line.strip():
	    print "find strcat in line %d" %(a)
	    ret = 1
	if "strcmp" in line.strip():
	    print "find strcmp in line %d" %(a)
	    ret = 1
	if "strcpy" in line.strip():
	    print "find strcpy in line %d" %(a)
	    ret = 1

    return ret

def startfind(files, dirs, root):
    for ii in files:
	try:
	    #print ii
	    if(findstring(root+"/"+ii) == 1):
		filelists.append(root+"/"+ii)
		print root+"/"+ii
		print ""
	except Exception as err:
	    print err
	    continue

    for jj in dirs:
	fi, di, ro = get_files(root+"/"+jj)
	startfind(fi, di, ro)

if __name__== '__main__':
    default_dir = sys.argv[1]
    file_path = default_dir
    files, dirs, root = get_files(default_dir)
    filelists = []
    startfind(files,dirs,root)
    print "Files include string functions:"
    for p in filelists:
	print p
	

#get_files()
