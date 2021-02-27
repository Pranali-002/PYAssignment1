#2. Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console. 

def Checksum(no):
	if (no%2==0):
		print("Number is even.")
		
	else:
		print("Number is odd.")
		
def main():
	print("Enter one number")
	value = int(input())
	Checksum(value)

if __name__ == "__main__":
	main()
