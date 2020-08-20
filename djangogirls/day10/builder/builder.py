from abc import ABCMeta, ABC
from abc import abstractmethod
from day10.builder.car import Car
from day10.builder.manual import Manual


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
    def set_transmission(self):
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

    def set_transmission(self, transmission):
        self.car.transmission = transmission

    def set_trip_computer(self, trip):
        self.car.trip = trip

    def set_gps(self, gps):
        self.car.gps = gps

    def get_result(self):
        return self.car


class CarManualBuilder(Builder, ABC):
    def __init__(self):
        self.manual = Manual()

    def reset(self):
        self.manual = Manual()

    def set_seats(self, number):
        self.manual.number_seats = number

    # ("Count of seats:" + str(number) + '\n'), number文字列をクラスに渡す。
    def set_engine(self, engine):
        self.manual.engine = engine
        # ("Engine:" + engine + '\n')


    def set_transmission(self, transmission):
        self.manual.transmission = transmission


    def set_trip_computer(self, trip):
        self.manual.trip = trip
        # ("Trip Computer:" + trip + "\n")

    def set_gps(self, gps):
        self.manual.gps = gps
        # ( + gps + "\n")

    def get_result(self):
        return self.manual
