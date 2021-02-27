#8. Write a program which accept number from user and print that number of “*” on screen. 

def Display(n):
	icnt =0
	for icnt in range(n):
		print("*",end= " ")
		
def main():
	print("Enter the number")
	no = int(input())
	Display(no)
	
if __name__ == "__main__":
	main()