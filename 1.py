import io
filee =io.open('1.txt', 'r+')
y="0"

print y
while 1 : 
		
	try :
		x= filee.readline()
		if x == "" :
			break
		else :
			print x
			y+=x
	except :
		break


print len(y)
x1= 0
x2= 0
i = 0 
j = 0
bb = 1
z = {}
while i < len(y): 
	if ((y[i] == " ") | (y[i] == "\n") ): 
		if(bb==0) :

			z[j] = y[x1:i]
			print y[x1:i]
			x1 = i 
			j = j + 1
			bb=1
		else : 
			x1=x1+1
			print "hacker "
	else :
		bb=0		
			
	i=i+1
	

n=input("omar")		
# Retrieve file contents -- this will be
# u'First line.\nSecond line.\n'


# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
print len(z)
i=0
while (i<j):
	print z[i]
	i=i+1





ch = "abcdefghijklmnopqrstuvwxyz1234567890"
print len(ch)
u=[36]
y={}

i=0
k=0
while i<j :
	v=z[i]
	while k<len(v)



filee.close()
