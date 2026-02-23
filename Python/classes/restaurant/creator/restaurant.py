from creator.rating import Rating

class Restaurant:
    '''Class Restaurant'''
    r_list = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False
        self._rating = []
        Restaurant.r_list.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    @classmethod
    def show_all(cls):
        print(f'{'NAME'.ljust(10)} | {'CATEGORY'.ljust(10)} | {'RATING'.ljust(10)} | {'ACTIVE'.ljust(10)}')
        for r in cls.r_list:
            print(f'{r._name.ljust(10)} | {r._category.ljust(10)} | {str(r.avg_rating).ljust(10)} | {r.active.ljust(10)}')

    @property
    def active(self):
        return '☑' if self._active else '☒'
    
    def toggle_active(self):
        self._active = not self._active
        
    def get_rating(self, client, rate):
        rating = Rating(client, rate)
        self._rating.append(rating)

    @property
    def avg_rating(self):
        if not self._rating:
            return 'Not rated'
        all_rate = sum(rating._rate for rating in self._rating)
        rate_amm = len(self._rating)
        avg_rate = round(all_rate / rate_amm, 1)

        return avg_rate
    