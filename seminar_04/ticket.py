class Ticket:
    def __init__(self, price, date, start_zone, finish_zone, luggage, place, road_number):
        self.__price = price
        self.__date = date
        self.__start_zone = start_zone
        self.__finish_zone = finish_zone
        self.__luggage = luggage
        self.__place = place
        self.__road_number = road_number

    def get_price(self):
        return self.__price

    def get_date(self):
        return self.__date
