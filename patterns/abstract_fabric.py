import random
from abc import ABC, abstractmethod

CATEGORIES = "ABCDE"


class Transport:
    def __init__(self, transport_type, driver=None):
        self.transport_type = transport_type
        self.list_of_passengers = []
        self.driver = driver

    def go(self):
        if self.driver is not None and len(self.list_of_passengers) > 0:
            print(f'{self.transport_type} go')
        elif len(self.list_of_passengers) == 0:
            raise ValueError("Подождём пока заполнимся")
        else:
            raise ValueError("Где водитель?")

    def take_passengers(self, list_of_passengers):
        if self.transport_type == 'taxi' and len(self.list_of_passengers) + len(list_of_passengers) > 3:
            raise ValueError("Уже есть пассажиры, новые влезут не все")

        elif self.transport_type == 'bus' and len(self.list_of_passengers) + len(list_of_passengers) > 39:
            raise ValueError("Уже есть пассажиры, новые влезут не все")
        else:
            self.list_of_passengers.extend(list_of_passengers)

    def take_driver(self, driver):
        if self.driver is not None:
            raise ValueError("Уже есть водитель")
        else:
            if driver.category > "A" and self.transport_type == 'taxi':
                self.driver = driver
            elif self.transport_type == 'taxi':
                raise ValueError(f"Не хватает квалификации, ожидалась B, "
                                 f"имеется {driver.category}")
            elif self.transport_type == 'bus' and driver.category >= 'D':
                self.driver = driver
            else:
                raise ValueError(f"Не хватает квалификации, ожидалась D,"
                                 f" имеется {driver.category}")


class BoardAnyCar(ABC):
    """Abstract class for create drivers and passengers"""

    @abstractmethod
    def board_driver(self):
        pass

    @abstractmethod
    def board_passenger(self):
        pass


class BoardTaxi(BoardAnyCar):
    """fabric class for create drivers and passenger for taxi"""

    def board_driver(self):
        return TaxiDriver(CATEGORIES[random.randint(0, 4)])

    def board_passenger(self):
        return [Passenger() for _ in range(3)]


class BoardBus(BoardAnyCar):
    """fabric class for create drivers and passenger for bus"""

    def board_driver(self):
        # return BusDriver(CATEGORIES[4])
        return BusDriver(CATEGORIES[random.randint(0, 4)])

    def board_passenger(self):
        return [Passenger() for _ in range(30)]


class Driver(ABC):
    def __init__(self, category):
        self.category = category

    def sit_in_car(self, car):
        car.take_driver(car, self)


class BusDriver(Driver):
    def __init__(self, category):
        super().__init__(category)


class TaxiDriver(Driver):
    def __init__(self, category):
        super().__init__(category)


class Passenger:
    id = 0

    def __init__(self):
        self.id = Passenger.id
        Passenger.id += 1


if __name__ == "__main__":
    taxi = Transport("taxi")
    bus = Transport("bus")
    taxi.take_driver(BoardTaxi().board_driver())
    bus.take_driver(BoardBus().board_driver())
    bus.take_passengers(BoardBus().board_passenger())
    taxi.take_passengers(BoardTaxi().board_passenger())
    taxi.go()
    bus.go()
