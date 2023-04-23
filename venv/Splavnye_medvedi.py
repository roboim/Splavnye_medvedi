class KayakingRoute:
    def __init__(self, river_name, area, start_point, coord_start_point, end_point, coord_end_point,
                 distance_km, year_journey, qty_days, distance_from_city, feature,
                 camping_places, coord_camping_places, picture_links ):
        self.river_name = river_name
        self.area = area
        self.start_point = start_point
        self.coord_start_point = coord_start_point
        self.end_point = end_point
        self.coord_end_point = coord_end_point
        self.distance_km = distance_km
        self.year_journey = year_journey
        self.qty_days = qty_days
        self.distance_from_city = distance_from_city
        self.feature = feature
        self.camping_places = camping_places
        self.coord_camping_places = coord_camping_places
        self.picture_links = picture_links


    def route_weather(self, start_date, forecast_duration = 4):
        print('надо добавить')


route1 = KayakingRoute('Суна', 'Карелия','Поросозеро', '62.718594, 32.697102', 'Линдозеро', '62.437217, 33.259267',
                        50.0, 2022, 4.0, 1100.0, '1 день катались на пороге',
                        'много', 'нет', 'нет')
print(route1.__dict__)
print("Test")