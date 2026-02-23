from creator.restaurant import Restaurant

gomery_restaurant = Restaurant('Gomery', 'Gourmet')
gomery_restaurant.get_rating('Alex', 100)
gomery_restaurant.get_rating('Lary', 4.3)
gomery_restaurant.get_rating('Jhonny', 3.2)

plaza_restaurant = Restaurant('Plaza', 'Pizza')

plaza_restaurant = Restaurant('Meadow', 'Mexican')

def main():
    Restaurant.show_all()

if __name__ == '__main__':
    main()

