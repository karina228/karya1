

def caesar(cryptMode):
	startMessage = input("Write the message: ").upper()
	try:rotKey = int(input("Write the key: "))
	except ValueError: print("Only numbers!"); raise SystemExit
	final = ""
	for symbol in startMessage:
		if cryptMode == 'E': 
			final += chr((ord(symbol) + rotKey - 13)%26 + ord('A'))
		else: 
			final += chr((ord(symbol) - rotKey - 13)%26 + ord('A'))
	print("Final message: " + final)