class exception:
    def __init__(self,num1):
        self.num1 = num1
    
    def compute(self):
        num1 = int(input("enter the  number"))
class ValueTooHigh(exception):
    def __init__(self, num1):
        super().__init__(num1)
    try:
        if num1 > 100: 
            raise ValueTooHighError as e
        else :
            print("the  number is below 100")
    except ValueTooHighError:
        print("you can not divide with zero")
    