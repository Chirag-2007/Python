#Ulta Order
def printNto1(n):
    #base case
    if n == 0:
        return
    
    print(n)
    #recursive case
    printNto1(n-1)

printNto1(5)

#Sidtha Order
def printNto1(n):
    #base case
    if n == 0:
        return
    
    printNto1(n-1)
    print(n)
    

printNto1(5)