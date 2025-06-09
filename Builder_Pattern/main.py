from ComputerTypes.OfficeComputer import OfficeComputer
from ComputerTypes.GamingComputer import GamingComputer


type = input("Type the computer you want(gaming, office): ").lower()

if type == 'gaming':
    computer = GamingComputer.construct()
    print(computer.construction())
elif type == 'office':
    computer = OfficeComputer.construct()
    print(computer.construction())
else:
    print('Invalid type')