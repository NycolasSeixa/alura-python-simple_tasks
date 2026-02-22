import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from restaurant import Restaurant

gomery_restaurant = Restaurant('Gomery', 'Gourmet')
meadow_restaurant = Restaurant('Meadow', 'Mexican')
meadow_restaurant.toggle_active()

def main():
    Restaurant.show_all()

if __name__ == '__main__':
    main()

