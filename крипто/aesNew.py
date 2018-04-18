
def aesnew(cryptMode):
	import pyAesCrypt
	from os import remove
	from os.path import splitext
	fileName = input("Write the file: ")
	paswFile = input("Write the password: ")
	bufferSize = 64*1024
	final = ""
	if cryptMode == 'E':
		try: 
			pyAesCrypt.encryptFile(str(fileName), str(fileName)+".crp", paswFile, bufferSize)
			remove(fileName)
		except FileNotFoundError: return "[x] File not found!"
		else: return "[+] File '"+str(fileName)+"' overwritten!"
	else:
		try: 
			pyAesCrypt.decryptFile(str(fileName), str(splitext(fileName)[0]), paswFile, bufferSize)
			remove(fileName)
		except FileNotFoundError: return "[x] File not found!"
		except ValueError: return "[x] Password is False!"
		else: return "[+] File '"+str(splitext(fileName)[0])+".crp' overwritten!"
	print(final)