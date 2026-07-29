class Complex:
  def __init__(self,real,img):
    self.real = real
    self.img = img
  def show_num(self):
    print(self.real,"i+",self.img,"j")
  def __add__(self,num2):
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal,newImg)
#we can write a+b as a__add__(b) which is a Dunder functions
  def __sub__(self,num2):
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal,newImg)

num1 = Complex(2,3)
num1.show_num()

num2 =Complex(1,4)
num2.show_num()

num3 = num1 + num2
num3.show_num()

num4 = num1 - num2
num4.show_num()

