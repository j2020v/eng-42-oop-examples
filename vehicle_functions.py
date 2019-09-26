class Vehicle:

    def __init__(self, model='', number_plate='', color='', wheels=4, doors= 4, passenger=7):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.passenger = passenger
        self.number_plate = number_plate
        self.color = color


    def accelarate(self):
        return ('VROOOOOOOOOM')
    def brk(self):
        return ('EEEEEEEEEEK stop')
    def turn(self):
        return ('SKRR SKRR')
    def play_music(self):
        return ('BOOM BOOM POW')
