class Car(object):
    def __init__(self, speed, model, brand, color) :
        self.speed = speed
        self.model = model
        self.brand = brand
        self.color = color
    def start(self):
        print("started")
    def stop(self):
        print('stopped')
    def accelarate(self):
        print('accelarating accelarator functionality here')
    def change_gear(self,gear_type):
        print('gear changed gear related functionality here')
        
audi = Car(80, 'A6', 'Audi', 'black')

print(audi.start)