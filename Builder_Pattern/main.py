from ComputerTypes import GamingComputer, OfficeComputer


type = input("Type the computer you want(gaming, office): ").lower()

if type == 'gaming':
    computer = GamingComputer.construct()
    print(computer.construction())
elif type == 'office':
    computer = OfficeComputer.construct()
    print(computer.construction())
else:
    print('Invalid type')