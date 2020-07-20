class Director:
    def __init__(self):
        self.__builder = None

    def makeSUV(self):
        pass

    def make_sports_car(self, builder):
        self.__builder = builder
        self.__builder.reset()
        self.__builder.set_seats(2)
        self.__builder.set_engine('volume - 3.0; mileage - 0.0' + '\n' + 'Transmission: SEMI_AUTOMATIC')
        self.__builder.set_trip_computer('Functional')
        self.__builder.set_gps('Functional')
