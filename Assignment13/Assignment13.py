import sys
import os
import schedule
import time
import Checksum
import psutil
import urllib.request as urllib
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
	try:
		urllib.urlopen('http://216.58.192.142',timeout=1)
		return True
	except urllib.URLError as err:
		return False
		
def MailSender(filename, to):
	try:
		fromaddr = "sanketw8448@gmail.com"
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = to
		body = """
		Hello %s.
		
		Please find attached document which contains List of Deleted Duplicate Files.
		
		This is AUTO generated mail.
		
		Thanks & Regards,
		Sanket Wadekar
		"""%(to)
		
		Subject = "Duplicate Files Removal"
		
		msg['Subject'] = Subject
		
		msg.attach(MIMEText(body,'plain'))
		
		attachment = open(filename,"rb")
		
		p = MIMEBase('application','octet-stream')
		
		p.set_payload((attachment).read())
		
		encoders.encode_base64(p)
		
		p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
		
		msg.attach(p)
		
		s = smtplib.SMTP('smtp.gmail.com',587)
		
		s.starttls()
		
		s.login(fromaddr,"Ishika222")
		
		text = msg.as_string()
		
		s.sendmail(fromaddr,to,text)
		
		s.quit()
		
		print("File successfully sent through mail")
	
	except Exception as E:
		print("Unable to send mail",E)
		
def DuplicateRemoval(path,to):

	data = {}
	for folder,subfolder,files in os.walk(path):
		for name in files:
			name = os.path.join(folder,name);
			checksum = Checksum.hashfile(name)
			if checksum in data:
				data[checksum].append(name)
			else:
				data[checksum] = [name]
	
	
	filepath = os.path.join(path,"DuplicateFileRemoval.txt")
	seperator = "-"*80
	f = open(filepath,'w')
	f.write(seperator+"\n")
	f.write("Deleted Duplicate Files\n")
	f.write(seperator+"\n")
	f.write("\n")
	
	newdata = [];
	newdata = list(filter(lambda x: len(x)>1,data.values()))
	
	count = 0
	for outer in newdata:
		icnt = 0
		for inner in outer:
			icnt = icnt + 1
			if icnt > 1:
				count = count + 1
				os.remove(inner);
				f.write(inner+"\n")
	f.write("\nTotal files deleted: %d"%count)
	f.write("\n")
	f.close()
	
	connected = is_connected()
	
	if connected:
		MailSender("DuplicateFileRemoval.txt",to)
	else:
		print("There is no Internet Connection")
	
def main():
	try:
		schedule.every(int(sys.argv[2])).minutes.do(DuplicateRemoval,path = sys.argv[1],to = sys.argv[3])
		while True:
			schedule.run_pending()
			time.sleep(1)
	except Exception as E:
		print("Error in main")
		
if __name__ == '__main__':
	main()