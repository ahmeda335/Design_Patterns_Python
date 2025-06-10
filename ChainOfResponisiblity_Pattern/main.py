from dispenser_chain import ATMDispenserChain

atm = ATMDispenserChain()
amounts = [750, 150, 50]  # Must be multipier of 50. "TODO: You can handle it"

for amount in amounts:
    print(amount)
    atm.chain1.handle(amount)
    print('-' * 30)