import os

def main():
	filename = input("Enter filename : ")
	flag = bool(os.path.exists(filename))
	if flag:
		print("File exists")
	else:
		print("File not found")
	
if __name__ == '__main__':
	main()