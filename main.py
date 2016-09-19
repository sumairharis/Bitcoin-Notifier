import urllib2
import re
import time
import cookielib
import os
import sys

def CurrentRate():
   url= "https://www.google.co.in/search?q=bitcoin+to+inr"
   req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
   con = urllib2.urlopen( req )
   Text=con.read()
   position=re.search("1 Bitcoin =",Text)
   return float(Text[position.end():position.end()+9])


def SendSMS(Price):
   username = "98XXXXXXX" #Your WAY2SMS USER MOBILE NO
   passwd = "MYPASSWORD" #YOUR WAY2SMS PASSWORD

   message ="Price of Bitcoin is "+str(Price)+" Yo!" #remove ads
   number = "7204370020" #enter the reciever's no.
   message = "+".join(message.split(' '))
    #Logging into the SMS Site
   url = 'http://site24.way2sms.com/Login1.action?'
   data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
   #For Cookies:
   cj = cookielib.CookieJar()
   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # Adding Header detail:
   opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
   try:
      usock = opener.open(url, data)
   except IOError:
      print "\n[-] CAN NOT CONNECT TO SERVER...CHECK USERNAME AND PASSWORD AND INTERNET CONNECTION ALSO"
      raw_input("\n[-] PRESS ENTER TO EXIT")
      sys.exit(1)

   jession_id = str(cj).split('~')[1].split(' ')[0]
   send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
   send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
   #opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
   try:
      sms_sent_page = opener.open(send_sms_url,send_sms_data)
   except IOError:
      print "\n[-] ERROR WHILE SENDING THE SMS...PLEASE UPDATE THE CONTACT LIST"
      sys.exit(1)


while 1:
   Price=CurrentRate()
   if Price>38000.0:
      SendSMS(Price)
      #print("sent")
   time.sleep(1800)
