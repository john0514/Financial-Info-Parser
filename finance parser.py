# -*- coding: ANSI -*-
f=open('20180711-20170901.txt','r',encoding = 'ANSI')
fw=open('pay.txt','w')
s=f.readline()
cdsum=0
paysum=0
while s:
	#''.join(s)
	list = s.split()
	if len(list) > 3 and list[3]=="�ѢҴ���":
		#print(s)
		cdsum+= int( list[4].replace(',','').replace('.','') )
		fw.write(s)
	elif len(list) > 3 and list[3]=="ú�O":
		paysum+= int( list[4].replace(',','').replace('.','') )
		fw.write(s)
	
	#print(list)
	s=f.readline()

f.close()
cdsum /=100
str="�ѢҴ��� :%d\n" %(cdsum)
print(str)
fw.write(str)
paysum /=100
str="ú�O     :%d\n" %(paysum)
print(str)
fw.write(str)
print("SUM :%d"%(cdsum+paysum))
fw.write("SUM :%d\n" %(cdsum+paysum))
