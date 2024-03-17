array_str = input("Введите параметры по шаблону - (цель, начало диапазона, конец диапазона) через пробел: ").split()
array = [int(item) for item in array_str]
print(array)

class Azimuth():
    def __init__(self, Array):
        self.fArray = Array
        self.Array = Array
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
        print(f"Цель по направлению {self.fArray[0]} в диапазоне от {self.fArray[1]} до {self.fArray[2]} - {self.Flag}")


Started = Azimuth(array)