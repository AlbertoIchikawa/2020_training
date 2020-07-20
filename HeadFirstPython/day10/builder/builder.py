from abc import ABCMeta, ABC
from abc import abstractmethod
from day10.builder.car import Car


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_trip_computer(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass


class CarBuilder(Builder, ABC):
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_seats(self, number):
        self.car.number_seats = number

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self, trip):
        self.car.trip = trip

    def set_gps(self, gps):
        self.car.gps = gps

    def get_result(self):
        return self.car


class CarManualBuilder(Builder, ABC):
    def __init__(self):
        self.buffer = []

    def reset(self):
        return

    def set_seats(self, number):
        self.buffer.append("Count of seats:" + str(number) + '\n')

    def set_engine(self, engine):
        self.buffer.append("Engine:" + engine + '\n')

    def set_trip_computer(self, trip):
        self.buffer.append("Trip Computer:" + trip + "\n")

    def set_gps(self, gps):
        self.buffer.append("GPS Navigation:" + gps + "\n")

    def get_result(self):
        return ''.join(self.buffer)
