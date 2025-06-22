from Payment_Methods import PaymentInterface


class Context():
    @staticmethod
    def use_payment_method(payment_method: PaymentInterface, amount: float):
        print(payment_method(amount)())
        