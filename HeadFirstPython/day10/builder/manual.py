class Manual:
    def __init__(self):
        self.transmission = None
        self.number_seats = 0
        self.engine = None
        self.trip = None
        self.gps = None

    def get_seats(self):
        return self.number_seats

    def set_engine(self):
        return self.engine

    def set_transmission(self):
        return self.transmission

    def set_trip_computer(self):
        return self.trip

    def set_gps(self):
        return self.gps

    def __repr__(self):
        return (
            f'Count of seats: {self.number_seats!r}\n'
            f'Engine:{self.engine!r}\n'
            f'Transmission{self.transmission!r}\n'
            f'Trip Computer:{self.trip!r}\n'
            f'GPS Navigator:{self.gps!r}\n'
        )
