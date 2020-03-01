from random import randrange
import math


class Car:

        def __init__(self):
            self.speed = 0
            self.distance = 0
            self.acc_1 = 0
            self.acc_2 = 0

            self.speed_range = (20, 81)
            self.distance_range = (10, 150)
            self.accelerating = True
            self.acc_1_range = (1, 4)
            self.acc_2_range = (1, 4)

        def random_vars(self):
            self.acc_1 = randrange(*self.acc_1_range)
            self.acc_2 = randrange(*self.acc_2_range)

            self.speed = randrange(*self.speed_range)
            self.distance = randrange(*self.distance_range)


class  Def:
    def __init__(self):
        self.speed = 0
        self.acc_1 = 0
        self.acc_2 = 0
        self.full_dist = 0
        self.dist = 0
        self.light_time = 0

    def to_def (self, car, passing):
        car_dist = car.distance
        self.dist = car_dist

        self.acc_1 = car.acc_1
        self.acc_2 = car.acc_2

        self.speed = car.speed

        self.full_dist = car_dist + passing.l
        self.light_time = passing.light_time
        suggestion = self.calculate_decision()
        return suggestion

    def calculate_time_needed_accelerating(self, acc):
        t = ((-1*self.speed) + (math.sqrt((pow(self.speed, 2) + 2 * acc * self.full_dist)))) / acc
        return t

    def calculate_time_needed_decelerating(self, acc):
        t = (self.speed - (math.sqrt((pow(self.speed, 2) - 2 * acc * self.dist)))) / acc
        return t

    def calculate_decision(self):
        # First try accelerating
        time_needed = self.calculate_time_needed_accelerating(self.acc_1)
        time_needed_dec = self.calculate_time_needed_decelerating(self.acc_2)

        if time_needed < self.light_time:
            return "go fast"

        elif time_needed_dec < self.light_time:
            return "go slow"
        else:
            return "nither"

class IntersectionController:
    def __init__(self):
        self.intersection_width_range = (5, 21)
        self.light_time_range = (2, 6)
        self.l = 0
        self.light_time = 0

    def random_vars(self):
        self.width = randrange(*self.intersection_width_range)
        self.light_time = randrange(*self.light_time_range)

class MainControl:

    def __init__(self):
        # Create Car
        self.car = Car()
        self.intersection = IntersectionController()
        self.decision_controller = Def()

    # @staticmethod
    def define_variables(self):
        self.car.random_vars()
        self.intersection.random_vars()

    def to_def(self):
        return self.decision_controller.to_def(self.car, self.intersection)


if __name__ == "__main__":
    control = MainControl()
    control.define_variables()
    decision = control.to_def()
    print(decision)

