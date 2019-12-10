import os
import sys

def main():
	fw = open("demo.txt","w")
	fd = open(sys.argv[1],"r")
	fw.write(fd.read())
	
if __name__ == '__main__':
	main()