from multipledispatch import dispatch
class Calc(): # main class

    # same method in same class
    
    @dispatch(int,int) # solving overloading problem
    def Sum(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1+self.num2)

    @dispatch(int,int,int)
    def Sum(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        print(self.num1+self.num2+self.num3)

sum = Calc() # object of Calc class

sum.Sum(1,2) # output is 3
sum.Sum(1,2,3) # output is 6
