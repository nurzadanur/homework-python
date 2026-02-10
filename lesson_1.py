class Car :
    # construktor, initializer
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False
        #self.color = "red"
        #self.model = "foester"

    def drive_to(self, destination):
        if not self.fined:
            print(f"the car {self.model} is driving in", destination)
        else:
            print("the car was fine")


car_subaru = Car ( color="silver", model="Forester")
car_honda = Car ( color="black", model="accord")
print(car_subaru)
car_subaru.drive_to("bishkek")
print(car_honda) #тут где сохраняется
print("color, model: ",
      car_subaru.color,
      car_subaru.model) # here writing color and model to car
print("color, model: ",
      car_honda.color,
      car_honda.model)
car_subaru.color = "white"
print("color, model: ",
      car_subaru.color,
      car_subaru.model)
car_subaru.max_speed = 140
print(car_subaru.max_speed)
#print(car_honda.max_speed) # not writing bc there is no honda only subaru
print(type(car_subaru))  # тут какой тип here writing class
print(type("hello world")) # here writing type ex this is str