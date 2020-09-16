class Car:
    speed = 0
    color = 'EmptyColor'
    name = 'EmptyName'
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина начала движение')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction='вперёд'):
        print(f'Машина поехала {direction}')

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")


class TownCar(Car):
    def __init__(self, speed=Car.speed, color=Car.color, name=Car.name, is_police=Car.is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость автомобиля: {self.speed} ", 'Снизьте скорость до 59 км/ч')
        else:
            print(f"Текущая скорость автомобиля: {self.speed}")


class SportCar(Car):
    def __init__(self, speed=Car.speed, color=Car.color, name=Car.name, is_police=Car.is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed=Car.speed, color=Car.color, name=Car.name, is_police=Car.is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость автомобиля: {self.speed} ", 'Снизьте скорость до 39 км/ч')
        else:
            print(f"Текущая скорость автомобиля: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed=Car.speed, color=Car.color, name=Car.name, is_police=Car.is_police):
        super().__init__(speed, color, name, is_police)

#0 Инициализация объектов всех типов
NewTownCar = TownCar(61,'Black','BMW',True)
NewSportCar = SportCar(90,'Red','Honda')
NewWorkCar = WorkCar(41,'Golden','Mitsubishi',False)
NewPoliceCar = PoliceCar()
#1
NewTownCar.go()
NewTownCar.stop()
NewTownCar.turn() # По умолчанию - "Вперёд"
NewTownCar.show_speed()
print(f'Параметры городского автомобиля: Модель: {NewTownCar.name} '
      f', Цвет: {NewTownCar.color}, В розыске ли машина: {NewTownCar.is_police} ')
print('\n')
#2
NewSportCar.go()
NewSportCar.stop()
NewSportCar.turn('направо')
NewSportCar.show_speed()
print(f'Параметры спортивного автомобиля: Модель: {NewSportCar.name} '
      f', Цвет: {NewSportCar.color}, В розыске ли машина: {NewSportCar.is_police} ')
print('\n')
#3
NewWorkCar.go()
NewWorkCar.stop()
NewWorkCar.turn('налево')
NewWorkCar.show_speed()
print(f'Параметры рабочего автомобиля: Модель: {NewWorkCar.name} '
      f', Цвет: {NewWorkCar.color}, В розыске ли машина: {NewWorkCar.is_police} ')
print('\n')
#4
NewPoliceCar.go()
NewPoliceCar.stop()
NewPoliceCar.turn('назад')
NewPoliceCar.show_speed()
print(f'Параметры полицейского автомобиля: Модель: {NewPoliceCar.name} '
      f', Цвет: {NewPoliceCar.color}, В розыске ли машина: {NewPoliceCar.is_police} ')
print('\n')