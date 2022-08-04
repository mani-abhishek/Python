def DecimalToBinary(num):
    temp =[]
    while(num>=1):
        temp.append(num%2)
        num = num//2
    return temp



def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal) 

def printprisoner(n):
    for i  in range(1,n+1):
        print(f"    P{i}",end='')
    print()
    print(f"B1  ", end='')
    for i in range(1,n+1):
        print(f" 0",end='    ')
    print()

def appendwithZero(temp,l,size):
    for i in range(l,size):
        temp.append(0)
    return temp

def exceptionalCase(p):
    for i in range(1,p):
        print(f"0",end='     ')
    print("1")
    



def findPoison(bottle,prisoner):

    printprisoner(prisoner)
    ans =[]
    t = []
    for b in range(2,bottle+1):
       temp  = DecimalToBinary(b)
       
       print(f"B{b}   ", end='')
       if(prisoner>len(temp)):
        temp = appendwithZero(temp,len(temp),prisoner)

       if(2**prisoner == bottle and b == bottle):
        exceptionalCase(prisoner)
        continue
       l = len(temp)-1
       while(l>=0):
        # t.append(temp[l])
        print(temp[l],end='     ')
        l= l-1
       print()
    ans = binaryToDecimal(1000110111)
    # if 1 denotes prisoner testeed the bottle and 0 denotes prisoner not tested the bottle
    print("Poisoned Bottle = ",ans)
    

      

        




if __name__ == "__main__":
    # noOfBottle    = int(input("Enter number of bottle = "))
    # noOfPriosoner = int(input("Enter number of prisoner = "))
    noOfBottle   =1000 
    noOfPriosoner = 10  
    findPoison(noOfBottle,noOfPriosoner)
    
    
    