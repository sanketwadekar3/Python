import os

def main():
	filename = input("Enter filename : ")
	fd = open(filename)
	print(fd.read())
	
if __name__ == '__main__':
	main()