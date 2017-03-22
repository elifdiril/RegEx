#141101010,Elif Diril,Bil334
#!/usr/bin/python
import re
fo = open("code_output.txt", "w+")
with open('file2.txt') as fp:
    for line in fp:
	mat=re.match(r".*\s\w+\d+\-\d+\.\d+\s.*", line)
	if mat:
   		ef=re.match(r".* success",line)
		if ef:
			ed=re.match(r".* isbn.* .*",line)
			if ed:
				date=re.sub(r'/',"-",line)
				a= date.split(" ")
				res=a[0][:len(a[0])-2]+str(int(a[0][len(a[0])-2:])+2000)+" "+a[6][5:]+" "+a[5].capitalize()+" "+a[4]
				
	
			else:
				date=re.sub(r'/',"-",line)
				a= date.split(" ")
				res=a[0][:len(a[0])-2]+str(int(a[0][len(a[0])-2:])+2000)+" "+a[5].capitalize()+" "+a[4]
			fo.write( res+"\n" )
