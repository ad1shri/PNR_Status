from bs4 import BeautifulSoup
import mechanize
from views import *
br = mechanize.Browser()
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
#print len(mydivs),'\n'
for index in range(len(mydivs)):
	f.write(mydivs[index].text)

f.close()
