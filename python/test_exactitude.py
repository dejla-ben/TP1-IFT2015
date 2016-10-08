from ADDS1 import*
from ADDS2 import*
from ADDS3 import*


def testADDS1():
	for i in range(0,10):
                for j in range(0,10):
                        somme=i+j
                        if ADDS1(str(i),str(j))==(str(somme%10),str(somme//10)):
                                return True
                        else:
                                raise False

                                
def test2ADDS2():
        for i in range(0,10):
                for j in range(0,10):
                        somme=i+j
                        if ADDS2(str(i),str(j))==(str(somme%10),str(somme//10)):
                                return True
                        else:
                                return False
def testADDS3():
        for i in range(0,10):
                for j in range(0,10):
                        somme=i+j
                        if ADDS3(str(i),str(j))==(str(somme%10),str(somme//10)):
                                return True
                        else:
                                return False
        
        

