from character import Character


warrior = Character(health=100, strength=500, magic="Speed", weapon="Sword")
print(warrior)

print('-'*20, '2', '-' * 20)

warrior2 = warrior.clone(1)
print(warrior2)
warrior2.health = 80
print(warrior)
print(warrior2)

print('-'*20, '3', '-' * 20)

warrior3 = warrior.clone(2)
warrior3.health = 50
print(warrior)
print(warrior3)

print('-'*20, '4', '-' * 20)

warrior4 = warrior.clone(3)
warrior4.health = 30
print(warrior)
print(warrior4)