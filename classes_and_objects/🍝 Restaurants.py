class Restaurant:
  name = ''
  category = ''
  rating = 0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

sushi_han = Restaurant()
sushi_han.name = 'Sushi Han'
sushi_han.category = 'Japanese Cuisine'
sushi_han.rating = 4.9
sushi_han.delivery = True

turkish = Restaurant()
turkish.name = 'Turkish Doner Grill'
turkish.category = 'Turkish Cuisine'
turkish.rating = 4.8
turkish.delivery = True

print(vars(bobs_burgers))
print(vars(sushi_han))
print(vars(turkish))
