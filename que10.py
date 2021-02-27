#10. Write a program which accept name from user and display length of its name. 

def SLenght(no):
	i=0
	for icnt in no:
		i=i+1
	print("Lengh of string is:", +i)
	
def main():
	print("Enter the string:")
	n = input()
	SLenght(n)
	
if __name__ == "__main__":
	main()