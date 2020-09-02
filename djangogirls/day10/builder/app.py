from day10.builder.director import Director
from day10.builder.builder import CarBuilder, CarManualBuilder


if __name__ == "__main__":
    director = Director()
    builder = CarBuilder()
    director.make_sports_car(builder)
    car = builder.get_result()
    print("Car built:\n{}".format(car.get_seats()))

    print("Car manual built:\n")
    manual_builder = CarManualBuilder()
    director.make_sports_car(manual_builder)
    manual = manual_builder.get_result()
    print(manual)
