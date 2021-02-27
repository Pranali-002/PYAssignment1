#7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false. 

def Display(no):
	if(no%5 == 0):
		return True
	else:
		return False
		
def main():
	print("Enter the number:")
	value = int(input())
	
	div = Display(value)
	if div == True:
		print("True".format(value))
	else:
		print("False".format(value))
		
if __name__ == "__main__":
	main()