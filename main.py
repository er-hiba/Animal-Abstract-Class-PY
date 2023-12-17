from Animal import Animal, Horse, Cat, Dog

h1 = Horse("Jack", 4)
h2 = Horse("Steve", 5)

c1 = Cat("Nickie", 6)
c2 = Cat("Rosy", 4)
c3 = Cat("Riri", 2)

d1 = Dog("Rocky", 2)
d2 = Dog("Max", 3)

print("Horses:")
print("Sound:",h1.sound())
print(h1.info)
print(h2.info)

print("\nCats:")
print("Sound:",c1.sound())
print(c1.info)
print(c2.info)
print(c3.info)

print("\nDogs:")
print("Sound:",d1.sound())
print(d1.info)
print(d2.info)
