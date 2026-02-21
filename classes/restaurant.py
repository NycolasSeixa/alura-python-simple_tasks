class Restaurant:
    name = ''
    category = ''
    active = False 

plaza_restaurant = Restaurant()
plaza_restaurant.name = 'Plaza'
plaza_restaurant.category = 'Pizza'

if plaza_restaurant.active:
    print('Plaza is Active')
else:
    print('Plaza is Inactive')

biggy_restaurant = Restaurant()
biggy_restaurant.name = 'Biggy'
biggy_restaurant.category = 'Fast Food'
biggy_restaurant.active = True

print(biggy_restaurant)
print(dir(biggy_restaurant))
print(vars(biggy_restaurant))