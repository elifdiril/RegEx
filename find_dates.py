#141101010,Elif Diril,Bil334
#!/usr/bin/python
import re
fo = open("dates_output.txt", "w+")
with open('file.txt') as fp:
    for line in fp:
	mat=re.match(r'\d+/\d+/\d+', line)
	if mat:
		date=re.sub(r'/',"-",line)
		a= date.split(" ")
		res=a[0][:len(a[0])-2]+str(int(a[0][len(a[0])-2:])+2000)
		fo.write( res+"\n" )


