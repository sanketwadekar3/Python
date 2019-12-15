import os
import sys
import time
import psutil

def ProcessLog(pname):
	listprocess = []
	seperator = "-"*80
	f = open('ProcessLog.txt','w')
	f.write(seperator+"\n")
	f.write("Process Logger\n")
	f.write(seperator+"\n")
	f.write("\n")
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])
			listprocess.append(pinfo)
		except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
		
	count = 0
	print(pname)
	for element in listprocess:
		if(element['name'] == pname):
			f.write("%s\n"%element)
			count+=1
		
	if count == 0:
		f.write("No such process")
		
	print("Log file successfully generated")
	
def main():
	ProcessLog(sys.argv[1])

if __name__ == '__main__':
	main()
		
	