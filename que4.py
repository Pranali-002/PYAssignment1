#4.Write a program which display 5 times Marvellous on screen. 

def Display(value):
	iCnt = 0
	for iCnt in range(0,value):
		print("Marvellous")
		
def main():
	print("Enter the number of iteration")
	no = int(input())
	Display(no)
	
if __name__ == "__main__":
	main()