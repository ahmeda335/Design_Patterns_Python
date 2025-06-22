from context import Context
from Payment_Methods import PayPalPayment, CreditCardPayment, CryptoPayment

amount = 2000

context = Context()

# Paying using Credit Card
context.use_payment_method(CreditCardPayment, amount)

# Paying using Paypal 
context.use_payment_method(PayPalPayment, amount)

# Paying using Paypal 
context.use_payment_method(CryptoPayment, amount)
