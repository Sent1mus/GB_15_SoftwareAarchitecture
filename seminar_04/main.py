from seminar_04.person import Person
from seminar_04.ticket import Ticket

person = Person(1, "Иван", "1234567890", "password", "login")
ticket = Ticket(1000, "2023-12-05", "Zone1", "Zone2", False, "1", "Road1")

person.buy_ticket(ticket)
print(f"{person.get_name()} купил билет на {ticket.get_date()} за {ticket.get_price()} рублей")

