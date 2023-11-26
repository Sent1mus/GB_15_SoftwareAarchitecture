# Определение класса Point3D
class Point3D:
   # Конструктор класса, который принимает три аргумента: x, y и z
   def __init__(self, x, y, z):
       # Инициализация атрибутов класса
       self.x = x # Координата x
       self.y = y # Координата y
       self.z = z # Координата z

# Определение класса Angle3D
class Angle3D:
   # Конструктор класса, который принимает три аргумента: x_degrees, y_degrees и z_degrees
   def __init__(self, x_degrees, y_degrees, z_degrees):
       # Инициализация атрибутов класса
       self.x_degr = x_degr # Угол по оси x в градусах
       self.y_degr = y_degr # Угол по оси y в градусах
       self.z_degr = z_degr # Угол по оси z в градусах
