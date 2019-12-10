import os
import sys

def main():
	fd1 = open(sys.argv[1],"r")
	fd2 = open(sys.argv[2],"r")
		
	if (fd1.read() == fd2.read()):
		print("Success")
	else:
		print("Failure")
	
if __name__ == '__main__':
	main()