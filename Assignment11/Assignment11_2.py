import sys
import os
import hashlib

def hashfile(path, blocksize=1024):
	afile = open(path,'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf)>0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()
	
def DetectDuplicate(path):
	data = {}
	for folder,subfolder,files in os.walk(path):
		for name in files:
			name = os.path.join(folder,name)
			checksum = hashfile(name)
			if checksum in data:
				data[checksum].append(name)
			else:
				data[checksum] = [name]
				
	seperator = "-"*80
	f = open("DuplicateFile.txt",'w')
	f.write(seperator+"\n")
	f.write("Duplicate Files\n")
	f.write(seperator+"\n\n")
	
	newdata = []
	newdata = list(filter(lambda x: len(x)>1,data.values()))
	
	count = 0
	
	for outer in newdata:
		icnt = 0
		for inner in outer:
			icnt = icnt + 1
			if icnt > 1:
				count = count + 1
				f.write(inner+"\n")
	f.write("Total Duplicate Files are: %d"%count)
	f.write("\n")
	f.close()
	
def main():
	DetectDuplicate(sys.argv[1])
	
if __name__ == '__main__':
	main()