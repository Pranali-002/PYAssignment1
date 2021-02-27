#3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers. 

def Add(no1,no2):
	abc = no1 + no2
	return abc
	
def main():
	num1= int(input("Enter first number"))
	num2= int(input("Enter first number"))
	ans= Add(num1,num2)   
	print("Addition is:",ans)
	
if __name__ == "__main__":
	main()
	
