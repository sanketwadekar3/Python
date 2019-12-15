import os
import time
import psutil
import urllib.request as urllib
import smtplib
import sys
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
		Please find attached document which contains Log of Running Process.
		
		This is AUTO generated message.
		
		Thanks & Regards,
		Sanket Wadekar
		"""%(to)
		
		Subject = "Process log generator"
		
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
		
		print("Log file successfully sent through Mail")
		
	except Exception as E:
		print("Unable to send mail ",E)

def ProcessLog(log_dir,to):
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
	
	connected = is_connected()
	
	if connected:
		MailSender(log_path,to)
	else:
		print("There is no Internet Connection")
	
def main():
	ProcessLog(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
	main()
		
	