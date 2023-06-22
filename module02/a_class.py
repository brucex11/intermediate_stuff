
from email.utils import collapse_rfc2231_value


class Computer:

  def __init__( self, cpu1, ram1 ) -> None:
    self.cpu = cpu1
    self.ram = ram1

  def config(self):
    print(f'Config is: {self.cpu} {self.ram}' )
  
  def what_is_my_cpu(self):
    return self.ram
