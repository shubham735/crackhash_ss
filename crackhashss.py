import hashlib

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
	print('v1.0.0')

def checkintenmillion(word):
	with open('data/tenmillion.txt') as f:
		if word in f.read():
			print("true")
		else:
			print("false")

def readlineno(no):
	f=open('data/tenmillion.txt')
	lines=f.readlines()
	print(lines[no+1])

def getlineno(inp, filename):
    with open(filename,'r') as f:
        for (i, line) in enumerate(f):
            if inp+'\n' in line:
                return i+1
    return -1

def convert(filename):
	file2write=open('data/md5.txt','w')
	with open(filename) as f:
		content = f.readlines()
		for i in content:
			file2write.write(hashlib.md5(i.encode('utf-8')).hexdigest()+'\n')
	file2write.close()

def takeinput():
	print('Enter the text')
	word=input()
	return word

def main_imp():
	banner()
	word=takeinput()
	word.strip()
	if len(word)==32:
		print('It seems to be given string is in md5 format')
		no=getlineno(word,'data/md5.txt')
		if no== -1:
			print('Entered string is not a common password in top 10 million,  :(')
		else:
			readlineno(no)
	else:
		print('We are limited to md5 hashes only.Please check in future update versions.')
	# convert('data/tenmillion.txt')

def main():
	print('hello')

if __name__ == "__main__":
    main()
# checkintenmillion('hello')
# inp=int(input('Enter line no.'))
# readlineno(inp)
# inp=input('Enter word')
# print(getlineno(inp,'tenmillion.txt'))