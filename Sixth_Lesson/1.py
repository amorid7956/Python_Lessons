import time, random

colors = ['red', 'yellow', 'green']


class TrafficLight:
    __color = "red"

    def running(self):
        if self.__color == "red":  # сделал self.__color, а не TrafficLight.__color т.к
            # в рамках данного задания всё равно мы создаём только один объект
            print("Горит красный цвет", self.__color)
            time.sleep(7)
            self.__color = random.choice(colors)
            if self.__color != "yellow":
                print('Нарушение порядка режимов. Выход из программы')
                self.__color = ''
        if self.__color == "yellow":
            print("Горит желтый цвет", self.__color)
            time.sleep(2)
            self.__color = random.choice(colors)
            if self.__color != "green":
                print('Нарушение порядка режимов. Выход из программы')
                self.__color = ''
        if self.__color == "green":
            print("Горит зелёный цвет", self.__color)
            time.sleep(5)
            self.__color = "green"
            print("Конец!")


obj = TrafficLight()
obj.running()
