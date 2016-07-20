#from view import *
from new import mydivs 

f = open('data1','w')
f.write(len(mydivs))
for index in range(len(mydivs)):
	f.write(mydivs[index].text)

f.close()