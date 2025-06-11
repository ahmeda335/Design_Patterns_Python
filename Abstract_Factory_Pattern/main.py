from Factories import ToyotaFactory, BMWFactory


vechile = input("Enter the vechile: ").lower()

# Enter the vechile in that shape "{car_type} car" e.x: toyota car, toyota bike, toyota truck, bmw car, ..

if 'toyota' in vechile:
    vechile, _ = ToyotaFactory().get_vechile(vechile)
    print(vechile.get_specs()) if _ else print(vechile)
elif 'bmw' in vechile:
    vechile, _ = BMWFactory().get_vechile(vechile)
    print(vechile.get_specs()) if _ else print(vechile)
else:
    print("No vechile found")