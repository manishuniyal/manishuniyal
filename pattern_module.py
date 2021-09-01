from abc import ABC,abstractmethod
from math import factorial
n=int(input())

class Fun1:
    def fun1(self):
        for i in range(n):
            for j in range(n*3-i-1):
                print(" ", end="")


            for j  in range(i*2+1):
                print("*", end="")
            print("")

        c=n
        for i in  range (n):
            c-=1
            for j in range(n*2):
                print(" ", end="")
        
            for j in range(i):
                print(" ",end="")
            for j in  range(c*2+1,0,-1 ):
                print("*", end="")

            
            print("")


class Fun2:
    def __fun2(self,n=5):
        
        for i in range(n):
            for j in range(i):
                print("*", end="")
            print("")    
        for i in range(n):
            n-=1
            for j in range(n,0,-1):
                print("*", end="")
            print("") 
    def __factorial(self , n):
        # return 1 if (n==0 or n==1) else self.__factorial(n-1)*n
        if n==0 or n==1:
            return 1
        else:
            return self.__factorial(n-1)*n 

    def pub_fact(self, n):
        return self.__factorial(n)        

    def pub(self, t):
            return self.__fun2(t)



class Fun3 ():
    def __init__(self):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")

            for i  in range(i+1):
                print("*", end="") 
            print("")    
      



class Pascal(ABC):
    @abstractmethod
    def pascal(self):pass

class Fun4(Fun1,Fun2,Fun3, Pascal ):
    def pascal(self):
        for i in range(n):
            
            for j in range(n-i+1):

                # for left spacing
                print(" ", end="  ")

            for j in range(i+1):

                # nCr = n!/((n-r)!*r!)
                print(factorial(i)//(factorial(j)*factorial(i-j)), end="      ")

            # for new line
            print()

    def fun4(self):

        c=n
        for i in  range (n):

            c-=1
            for j in range(n*2):
                
                print(" ", end="")
        
            for j in range(i):
                print(" ",end="")
            for j in  range(c*2+1,0,-1 ):
                print("*", end="")
            
            print("")
        for i in range(n):
            for j in range(n*3-i-1):
                print(" ", end="")

            for j  in range(i*2+1):
                print("*", end="")
            print("")
    def t(): 
        pass       

 # Print Pascal's Triangle in Python

'''
f4=Fun4()
print("Factorial of {} is {}".format( n, f4.pub_fact(n)))

f4.pascal()
f4.fun1()
f4.fun4()
f4.pub(n)
'''

output1= [i for i in range(n) if i%2==0 ]
output2={i:i**3 for i in range(n) if i%2!=0 }
print(output2)