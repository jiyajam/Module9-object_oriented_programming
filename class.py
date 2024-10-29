#########1
class Car:

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def getregistration_number(self):
        return self.registration_number
    def getmax_speed(self):
        return self.max_speed

    def getcurrent_speed(self):
        return self.current_speed

    def gettravelled_distance(self):
        return self.travelled_distance

    def __str__(self):
        return f'{self.registration_number} , {self.max_speed}, {self.current_speed}, {self.travelled_distance}'

car1 = Car("ABC-123", "142km/h" )
print(f" the car's registration number is  {car1.registration_number}, the maximum speed is {car1.max_speed}, the current speed is {car1.current_speed} and the travelled distance is {car1.travelled_distance}")

########2
class Car:

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

car1 = Car("ABC-123",142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print (f"the current speed is {car1.current_speed}km/h")
car1.accelerate(-200)
print(f"The final speed after braking is {car1.current_speed} km/h")

#########3
class Car:

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 60
        self.travelled_distance = 2000

    def accelerate(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive (self,hours):
       travelled_distance = self.current_speed * hours
       self.travelled_distance += travelled_distance


car1 = Car("ABC-123",142)

car1.drive(1.5)

print(f"Current Speed: {car1.current_speed} km/h")
print(f"Travelled Distance: {car1.travelled_distance} km")


##########4

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration_number, max_speed))


during_race = True
while during_race:
    for car in cars:

        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)


        car.drive(1)


        if car.travelled_distance >= 10000:
            during_race = False
            break
print("-------"* 13 )
print("| Registration number | Max Speed (km/h) | Current Speed (km/h) | Travelled Distance (km) |")
print("-------"* 13 )
for car in cars:
    print(f"| {car.registration_number:<19} | {car.max_speed:<16} | {car.current_speed:<20} | {car.travelled_distance:<23.2f} |")

print("-------"* 13 )




