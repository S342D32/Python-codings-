from abc import ABC, abstractmethod
class FundTransfer:
  def __init__(self,acc_num,balance):
    self.acc_num = acc_num
    self.balance = balance
  @property
  def acc_num(self):
    return self.__acc_num

  @acc_num.setter
  def acc_num(self,acc_num):
    if len(str(acc_num)) == 10:
      self.__acc_num =acc_num
  
  @property
  def balance(self):
    return self.__balance

  @balance.setter
  def balance(self,balance):
    if balance>0:
      self.balance =balance
  def validate(self,amount):
    return (len(str(self.acc_num))==10 and amount<self.__balance and amount>0)
  @abstractmethod
  def transfer(self,amount):
    pass
class NEFTransfer(FundTransfer):
  def __init__(self,acc_num,balance):
    super().__init__(acc_num,balance)
  def transfer(self,amount):
    sc =amount *0.05
    if(amount + sc ) < self.balance:
      self.balance -= (amount + sc)
      return True
    return False
class IMPSTransfer(FundTransfer):
  def __init__(self,acc_num,balance):
    super().__init__(acc_num,balance)
  def transfer(self,amount):
    sc = amount * 0.02
    if (amount +sc) < self.balance:
      self.balance -= (amount + sc)
      return True
    return False
class RTGSTransfer(FundTransfer):
  def __init__(self,acc_num,balance):
    super().__init__(acc_num,balance)
    def transfer(self,amount):
      if amount < self.balance and amount > 10000:
        self.balance -= amount
        return True
      return False
def main():
  acc_num = 1234567890
  balance = 100000
  transfer = NEFTransfer(acc_num,balance)
  print(transfer.transfer(5000))
main()





