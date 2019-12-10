import os
import sys

def main():
	fd1 = open(sys.argv[1],"r")
	f = fd1.read()
	count = 0
	for word in f.split(' '):
		if word == sys.argv[2]:
			count = count + 1
		
	if count > 0:
		print("Frequency is : ",count)
	else:
		print("String not found")
	
if __name__ == '__main__':
	main()