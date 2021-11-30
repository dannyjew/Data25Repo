from Snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


peter = Python()
patty = Python()
patty.venom = True
print(peter.venom)
print(patty.venom)





class Country:
    def __init__(self, name, climate, continent, language):
        self.name = name
        self.climate = climate
        self.continent = continent # or Europe
        self.language = language


collection_of_countries = ["England", "Spain", "France"]

class City(Country):
    def __init__(self, city_name, name, climate, continent, language):
        super().__init__(name, climate, continent, language)
        self.city_name = city_name


city_info = City("London", "UK", "Rainy", "Europe", "English")
