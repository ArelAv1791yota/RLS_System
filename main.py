from copy import deepcopy


array_str = input("Введите параметры по шаблону - (цель, начало диапазона, конец диапазона) через пробел: ").split()
array = [int(item) for item in array_str]

class Azimuth():
    def __init__(self, Array):
        self.Array = Array
        self.f = deepcopy(Array)
        self.Flag = False
        self.zero_circle()
        self.az_inSector()
        self.display_out()

    def zero_circle(self):
        if self.Array[1] > self.Array[2]:
            self.Array[1] = self.Array[1]-360
            self.Array[0] = self.Array[0]-360

    def az_inSector(self):
        if (self.Array[1] <= self.Array[0]) and (self.Array[0] <= self.Array[2]):
            self.Flag = True

    def display_out(self):
        print(f"Цель по направлению {self.f[0]} в диапазоне от {self.f[1]} до {self.f[2]} - {self.Flag}")


Started = Azimuth(array)