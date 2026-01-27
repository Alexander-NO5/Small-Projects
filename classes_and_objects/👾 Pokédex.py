class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
  
  def speak(self):
    print(f'{self.name} {self.name}')

  def display_details(self):
    if self.is_caught:
      catch_status = f'{self.name} has been already caught!'
    else:
      catch_status = f'{self.name} has not been caught!'

    print(f'Entry Number: {self.entry}\n'
          f'Name: {self.name}\n'
          f'Type: {self.types}\n'
          f'Description: {self.description}\n'
          f'{catch_status}')

pikachu = Pokemon(25, 'Pikachu', 'Electric', 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)

bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass, Poison', 'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.', False)

charmender = Pokemon(4, 'Charmender', 'Fire', 'The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.', True)

squirtle = Pokemon(7, 'Squirtle', 'Water', 'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.', True)

print('======================================================================================')
pikachu.display_details()
pikachu.speak()
print('======================================================================================')
bulbasaur.display_details()
bulbasaur.speak()
print('======================================================================================')
charmender.display_details()
charmender.speak()
print('======================================================================================')
squirtle.display_details()
squirtle.speak()
print('======================================================================================')
