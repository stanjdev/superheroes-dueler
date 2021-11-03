class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f'{self.name} is eating')

  def drink(self):
    print(f'{self.name} is drinking')


class Frog(Animal):
  def jump(self):
    print(f'{self.name} is jumping')

bouncer = Frog('bouncer')

bouncer.eat()
bouncer.drink()
bouncer.jump()

