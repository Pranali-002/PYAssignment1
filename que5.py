#5.Write a program which display 10 to 1 on screen. 

def Display():
	icnt=0
	for icnt in range(10,0,-1):
		print(icnt)
	else:
		print("end of loop")
		
def main():
	Display()

if __name__ == "__main__":
	 main()