class Car:
    total_cars = 0
    def __init__(self, name, model):
        self.__name = name # Private attribute - Applying underscore two times makes it private
        
        self.__model = model # Private attribute
        Car.total_cars += 1 # static variable to count the number of cars

    def getName(self):
        return self.__name
    
    @property # Decorator to define property
    def model(self): # model is used as property not as a method
        return self.__model

    def fullname(self):
        return f"{self.__name} {self.__model}"
    
    # Static method -- only access by class name
    @staticmethod # Decorator to define static method
    def generate_description():
        return "Car is a means of transport." 

car = Car("Toyota", "Corolla")
print(car.getName()) # Output: Toyota
print(car.model) # Output: Corolla
print(car.fullname()) # Output: Toyota Corolla

### Inheritance
class ElectricCar(Car):
    def __init__(self, name, model, batterySize):
        super().__init__(name, model)
        self.batterySize = batterySize


my_tesla_car = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla_car.fullname()) # Output: Tesla Model S

## Instance of ElectricCar is also instance of Car
print(isinstance(my_tesla_car, ElectricCar)) # Output: True
print(isinstance(my_tesla_car, Car)) # Output: True

print(f"Total Cars: {Car.total_cars}")
print(Car.generate_description()) # Output: Car is a means of transport.
print(my_tesla_car.generate_description()) # Output: Car is a means of transport.
print(car.generate_description()) # Output: Car is a means of transport.