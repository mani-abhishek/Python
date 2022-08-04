def DecimalToBinary(num):
    temp =[]
    while(num>=1):
        temp.append(num%2)
        num = num//2
    return temp

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

      

        




if __name__ == "__main__":
    noOfBottle = int(input("Enter number of bottle = "))
    noOfPriosoner = int(input("Enter number of prisoner = "))
    
    findPoison(noOfBottle,noOfPriosoner)
    
    