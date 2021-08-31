import math
import pytest
def test_gcm(a,b):
    if a==0:
        return b
    c=math.gcd(a,b)== test_gcm(b%a,a)
    return test_gcm(b%a,a)
def lcm(a,b):
    pro=a*b
    hcf=test_gcm(a,b)
    return pro//hcf
a=int(input())
b=int(input())
print("enter two number for\n  hcf {}  &lsm{}\n {}\n ".format(test_gcm(a,b), lcm(77,11),22//33))

