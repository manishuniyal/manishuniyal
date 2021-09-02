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
        print("abstract method")

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

        

 
f4=Fun4()
f4.pascal()
