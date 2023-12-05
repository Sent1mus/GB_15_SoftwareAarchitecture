class Person:
    def __init__(self, person_id, name, card_number, password, login):
        self.__person_id = person_id
        self.__name = name
        self.__card_number = card_number
        self.__password = password
        self.__login = login
        self.__tickets = []

    def buy_ticket(self, ticket):
        self.__tickets.append(ticket)

    def get_person_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_login(self):
        return self.__login

    def set_login(self, login):
        self.__login = login

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
