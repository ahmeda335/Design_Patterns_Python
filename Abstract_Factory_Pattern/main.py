from Factories.ToyotaFactory.toyota_factory import ToyotaFactory
from Factories.BMWFactory.BMW_factory import BMWFactory


vechile = input("Enter the vechile: ").lower()

if 'toyota' in vechile:
    vechile = ToyotaFactory().get_vechile(vechile)
    print(vechile.get_specs())
elif 'bmw' in vechile:
    vechile = BMWFactory().get_vechile(vechile)
    print(vechile.get_specs()) 
else:
    print("No vechile found")