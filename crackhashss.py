import hashlib,string

def banner():
	print('''
	                          o      o                  o                          
	                          O     O                  O                           
	                          o     o                  o                           
	                          o     O                  O                           
	.oOo  `OoOo. .oOoO' .oOo  O  o  OoOo. .oOoO' .oOo  OoOo.           .oOo  .oOo  
	O      o     O   o  O     OoO   o   o O   o  `Ooo. o   o           `Ooo. `Ooo. 
	o      O     o   O  o     o  O  o   O o   O      O o   O               O     O 
	`OoO'  o     `OoO'o `OoO' O   o O   o `OoO'o `OoO' O   o           `OoO' `OoO' 
	                                                         ooooooooo            
		''')
	print('v0.2.0')
	

def checkintenmillion(word):
	with open('data/tenmillion.txt') as f:
		if word in f.read():
			print("true")
		else:
			print("false")

def readlineno(no):
	f=open('data/tenmillion.txt')
	lines=f.readlines()
	print(lines[no-1])

def getlineno(inp, filename):
    with open(filename,'r') as f:
        for (i, line) in enumerate(f):
            if inp+'\n' in line:
                return i+1
    return -1

def convert(filename):
	file2write=open('data/sha256.txt','w')
	with open(filename) as f:
		content = f.readlines()
		lists=[]
		for e in content:
			lists.append(e.strip())
		for i in lists:
			file2write.write(hashlib.sha256(i.encode('utf-8')).hexdigest()+'\n')
	file2write.close()

def takeinput():
	print('Enter the text')
	word=input()
	return word

def check(word):
	for letter in word:
		if letter not in string.hexdigits:
			return False
	return True

def main():
	banner()
	word=takeinput()
	word.strip()
	no=0
	if check(word):
		if len(word)==32:
			print('It seems to be given string is in md5 format')
			no=getlineno(word,'data/md5.txt')
		elif len(word)==40:
			print('It seems to be given string is in sha1 format')
			no=getlineno(word,'data/sha1.txt')
		elif len(word)==64:
			print('It seems to be given string is in sha3_256 format')
			no=getlineno(word,'data/sha3_256.txt')
		elif len(word)==96:
			print('It seems to be given string is in sha3_384 format')
			no=getlineno(word,'data/sha3_384.txt')
		# elif len(word)==128:
		# 	print('It seems to be given string is in sha3_512 format')
		# 	no=getlineno(word,'data/sha3_512.txt')
		elif len(word)==64:
			print('It seems to be given string is in sha256 format')
			no=getlineno(word,'data/sha256.txt')
		elif len(word)==96:
			print('It seems to be given string is in sha384 format')
			no=getlineno(word,'data/sha384.txt')
		# elif len(word)==128:
		# 	print('It seems to be given string is in sha512 format')
		# 	no=getlineno(word,'data/sha512.txt')
		else:
			print('We are limited to md5 hashes only.Please check in future update versions.')
	else:
		print('It does\'nt seems to be valid hash')
	
	if no== -1:
		print('Entered string is not a common password in top 10 million,  :(')
	else:
		print(readlineno(no))	

# def main():
# 	convert('data/tenmillion.txt')
	# print(hashlib.algorithms_guaranteed)


if __name__ == "__main__":
    main()
