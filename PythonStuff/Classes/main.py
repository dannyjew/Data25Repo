# class Dog:
# #
# #     def __init__(self, name, colour):
# #         self.__animal_kind = "canine"
# #         self.name = name
# #         self.colour = colour
# #         self.bark()
# #
# #     def bark(self):  # method
# #         print("woof")
# #
# #
# # # Draco = Dog("Draco","Black")
# # # Draco.animal_kind = "Cat"
# # # print(Draco.animal_kind)

class Car:

    def __init__(self, colour, max_speed):
        self.current_speed = 0
        self.colour = colour
        self.max_speed = max_speed
        deleteme = 2

    def accelerate(self, speed_to_accelerate):
        if self.current_speed + speed_to_accelerate > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_to_accelerate
        return self.current_speed

    def decelerate(self, speed_to_accelerate):



Zohrehs_Car = Car("Purple", 200)
Dannys_Car = Car("Green", 1000)
print(f"Zohrehs car is currently going {Zohrehs_Car.current_speed} mph")
Zohrehs_Car.accelerate(150)
Dannys_Car.accelerate(20)
print(f"Zohrehs car is currently going {Zohrehs_Car.current_speed} mph")
Zohrehs_Car.accelerate(70)
print(f"Zohrehs car is currently going {Zohrehs_Car.current_speed} mph")


class Customer:

    def __init__(self, customername, email, number):
        self.customername = customername
        self.email = email
        self.duration = 0
        self.send_welcome_email()
        self.enter_into_DB()

    def send_welcome_email(self):
        # sends email

    def enter_into_DB(self):
        #stores this info into database


Customer1 = Customer("Megan", "123@123.com", "0129301293")


