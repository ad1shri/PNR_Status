from bs4 import BeautifulSoup
import mechanize
from views import *
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)
br.open('http://www.indianrail.gov.in/pnr_Enq.html')

response = br.response()

br.select_form('pnr_stat')
br.form['lccp_pnrno1'] = no
#br.form['lccp_pnrno1'] = '2319216989'
response = br.submit()
content = response.read()
 
soup = BeautifulSoup(content,"lxml")
mydivs = soup.findAll("td", { "class" : "table_border_both" })
f = open('data','w')
#print len(mydivs)
for index in range(len(mydivs)):
	f.write(mydivs[index].text)

f.close()
