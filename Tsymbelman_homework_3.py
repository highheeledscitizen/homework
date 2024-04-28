import random


class Car:
    def __init__(self, model, color):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color
        self.is_fuel = True if self.fuel else False
        if self.fuel <= 0:
            print('fuel it`s over in ', self.model)

    def move(self, distance):
        if self.is_fuel:
            self.trip_distance += distance
            self.fuel -= distance * 0.01
            if self.fuel <= 0:
                print('fuel it`s over in ', self.model)
                self.is_fuel = False


toyota = Car('avensis', 'grey')
mini = Car('cooper s', 'green')
audi = Car('a3', 'black')

race_dist = 0
desired_dist = 100

while race_dist < desired_dist:
    for car in [toyota, mini, audi]:
        car.move(random.randrange(0, 9))
        cur_dist = car.trip_distance
        if cur_dist >= desired_dist:
            print('car: ', car.model, ' win ', car.trip_distance, 'km')
            break
    if cur_dist >= desired_dist:
        break

for car in [toyota, mini, audi]:
    print('model: ', car.model, ' distance: ', car.trip_distance, ' level fuel: ', car.fuel.__round__(2))