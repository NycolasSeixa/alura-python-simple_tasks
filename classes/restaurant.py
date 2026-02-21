class Restaurant:
    r_list = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False
        Restaurant.r_list.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    @classmethod
    def show_all(cls):
        print(f'{'NAME'.ljust(5)} | {'CATEGORY'.ljust(10)} | {'ACTIVE'.ljust(5)}')
        for r in cls.r_list:
            print(f'{r._name.ljust(5)} | {r._category.ljust(10)} | {r.active.ljust(5)}')

    @property
    def active(self):
        return '☑' if self._active else '☒'
    
    def toggle_active(self):
        self._active = not self._active


plaza_restaurant = Restaurant('Plaza', 'Pizzeria ')
plaza_restaurant.toggle_active()
biggy_restaurant = Restaurant('Biggy', 'Fast Food ')

Restaurant.show_all()