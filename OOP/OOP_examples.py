class Car(object):
    """docstring for Car."""
    def __init__(self, color):
        super(Car, self).__init__()
        self.numOfWheels = 4
        self.make = "Honda"
        self.model = "Civic"
        self.color = color
        self.topSpeed = 400

    def honk():
        print("Beep Beep!")

    def description(self):
        print("The car has " + self.numOfWheels + " with a make of "
              + self.make + " and model " + self.model
              + ". The car has a " + self.color + " color and a top speed of " + self.topSpeed + ".")
