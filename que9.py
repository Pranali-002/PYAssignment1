#9. Write a program which display first 10 even numbers on screen

def DisEven(n):
	i=j=1
	while j<=n:
		if i%2 ==0:
			print(i)
			j=j+1
		i=i+1
			
def main():
	print("Enter the number")
	no = int(input())
	
	DisEven(no)
	
if __name__ == "__main__":
	main()