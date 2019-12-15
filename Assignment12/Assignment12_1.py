import os
import time
import psutil

def ProcessLog():
	listprocess = []
	seperator = "-"*80
	f = open('ProcessLog.txt','w')
	f.write(seperator+"\n")
	f.write("Process Logger")
	f.write(seperator+"\n")
	f.write("\n")
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])
			listprocess.append(pinfo)
		except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
		
	for element in listprocess:
		f.write("%s\n"%element)
		
	print("Log file successfully generated")
	
def main():
	ProcessLog()

if __name__ == '__main__':
	main()
		
	