from dog import Dog

my_dog = Dog('Rex', 'SuperDog')
print(my_dog.breed)
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

barko = Dog('Barko', 'Alaskan Malamute')
sitto = Dog('Sitto', 'Cocker Spaniel')
rollo = Dog('Rollo', 'Wiener Dog')

barko.bark()
sitto.sit()
rollo.roll_over()