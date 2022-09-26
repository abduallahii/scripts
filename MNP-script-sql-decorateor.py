import os
import datetime

f = open('tester.txt', 'r')
f1 = open('tester2.txt', 'w')
f2 = open('arch.txt', 'w')
for line in f :
	listing = str(line)
	if listing[0:2] == "01" :
		f1.write(listing[1:11] + ' ')
		f2.write(listing[1:11] + ' ') 
	elif listing[0:4] == "***" or listing[0:4] == "***" or listing[0:2] == "****":
		f1.write(listing[0:4] + '\n') 
		f2.write(listing[0:4] + '\n') 


f.close()


#NP acctivated  Sucess
Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y , %H:%M:%S')
os.rename(r'arch.txt',r'arch.txt_' + str(Current_Date) + '.txt')
