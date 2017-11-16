class Car(object):
  def __init__(self, manufacturer, model, colour, doors):
    self.manufacturer = manufacturer
    self.model = model
    self.colour = colour
    self.doors = int(doors)

  def set_colour(self):
    self.colour = input("New Car Colour: ")
    return self.colour

  def __str__(self):
    return "Manufacturer: " + str(self.manufacturer) + "\nModel: " + str(self.model) + "\nColour: " + str(self.colour) + "\nNumber of Doors: " + str(self.doors)

Car1 = Car(input("Manufacturer: "), input("Model: "), input("Colour: "), input("Number of Doors: "))
print(Car1)
Car1.set_colour()
print(Car1)
