import os
import sys
import time
import psutil

def ProcessLog(log_dir):
	listprocess = []
	
	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass

	log_path = os.path.join(log_dir,"ProcessLog.txt")
	seperator = "-"*80
	f = open(log_path,'w')
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

	for element in listprocess:
		f.write("%s\n"%element)
		
	print("Log file successfully generated")
	
def main():
	ProcessLog(sys.argv[1])

if __name__ == '__main__':
	main()
		
	