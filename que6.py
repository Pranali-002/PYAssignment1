#6.Write a program which accept number from user and check whether that number is positive or negative or zero.

def fun(no):
	if no>0:
		print("The number is positive")
	elif no<0:
		print("The number is negative")
	elif no==0:
		print("The number is zero")
		
def main():
	print("Enter the number")
	value = int(input())
	fun(value)
	
if __name__ == "__main__":
	main()
		