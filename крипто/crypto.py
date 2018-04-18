import caesarNew
import S_RSA
import aesNew

def main():
	while (True):
		cipher = input("Enter the cipher: [C]aesar, [R]SA, [A]ES - ").upper()
		cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
		if (cipher not in ['C','R','A']):
			print("Error: cipher is not Found!"); raise SystemExit
		if (cryptMode not in ['E','D']):
			print("Error: mode is not Found!"); raise SystemExit

		if (cipher == 'C'):
			caesarNew.caesar(cryptMode)
		elif (cipher == 'R'):
			S_RSA.s_rsa()
		elif (cipher == 'A'):
			aesNew.aesnew(cryptMode)
		else:
			break
if __name__ == "__main__":
	main()