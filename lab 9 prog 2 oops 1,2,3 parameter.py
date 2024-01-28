'''2.	Create a class Demo and also create method test () in it. Overload test () in four ways. 
First version takes no parameter, the second takes one integer parameter, and the third takes two
 integer parameters and fourth takes one double parameter. '''

class Demo:
    def test(self,p1=None,p2=None):
        
        if p1 != None and p2 == None and isinstance(p1,int):
            print('second vesion with one integer parameter : ',p1)
        elif p1 != None and p2 != None :
            print('third version with two integer parameter :',p1,p2)
        elif p1 != None and isinstance(p1,float):
            print('fourth version with one double parameter : ',p1)
        else:
            print('first vesion with no parameter')

a = Demo()
a.test()
a.test(1)
a.test(1,2)
a.test(4.5)
          

