from payment1 import Payment1
from Payment2Adapter import Payment2Adapter


amount = 1000
p1 = Payment1(amount)
p1.pay()

p2 = Payment2Adapter(amount)
p2.pay()