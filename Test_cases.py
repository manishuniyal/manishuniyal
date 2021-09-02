import pytest 
import pattern_module
n=pattern_module.n

@pytest.mark.Test
def test_fun1():
    assert pattern_module.output1== [i for i in range (n) if i%2==0]
    assert type(pattern_module.output1)== list
    


#@pytest.mark.fun2
def test_fun2():
    pass