class Calc(): # main class or parent class

    # same method in same class
    
    def Sum(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1+self.num2)

    def Sum(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        print(self.num1+self.num2+self.num3)

sum = Calc() # object of Calc class

sum.Sum(1,2,3) # output is 6
sum.Sum(1,2) # this output produced error because there are same method in same class it called method overloading