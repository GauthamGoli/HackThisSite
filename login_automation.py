""" This program has been written to login to the HTS site and goto the specific page  , read the source and extract the question, submit the answer.
This program can be suitably modified to submit any other mission's solution later on """

import mechanize
import cookielib
import uncaesershift  # this contains the simple algorithm for solving challenge 11

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()       # cookie handling
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)        # browser object settings
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)  #to prevent hanging

br.set_debug_http(True)
br.set_debug_redirects(True)     # debug information
br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')] #user agent

br.open('http://www.hackthissite.org')
 
br.select_form(nr=0)

br.form['username'] = 'i404i'    # fill in username
br.form['password'] = "*******"  # fill in ***** with the actual password

br.submit()

response = br.open('http://www.hackthissite.org/missions/prog/11/')  
text = response.read()

text = text[text.find('Generated String:')+18:text.find('Shift:')+9]      # extracting the question string
enc = text[:text.find('<')]

text = text[text.find('Shift:')+6:]
text = text[:text.find('<')]
shift = int(text)
enc+=str(shift)

br.select_form(name="submitform")      #selecting the form used to submit solution of the challenge

br.form['solution'] = uncaesershift.s(enc)  

br.submit()


