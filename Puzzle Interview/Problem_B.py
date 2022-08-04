# In each weighing, 2/3rd of coins will be removed out of verification process.

def main(n):
    count = 0 
    while(n>=1):
        count=count+1
        n =n-((n*2)/3)
    print("The minimum number weighings required = ",count-1)


if __name__ =="__main__":
    n=27
    # n = int(input("Enter Total number of coins: "))
    
    # n should be multiple of 3
    main(n)
