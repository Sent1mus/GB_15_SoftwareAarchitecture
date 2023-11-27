from service import *
# Класс Flash представляет собой вспышку/свет в 3D-сцене
class Flash:
   def __init__(self, location, angle, color, power):
       # location - это точка в 3D-пространстве
       # angle - это угол в 3D-пространстве
       # color - это цвет вспышки, представленный в формате RGB (255, 255, 255)
       # power - это мощность вспышки, представленная в виде float_number
       self.location = location
       self.angle = angle
       self.color = color
       self.power = power

   # Метод rotate используется для вращения вспышки
   def rotate(self, angle)-> None:
       pass

   # Метод move используется для перемещения вспышки
   def move(self, point)-> None:
       pass


# Класс Camera представляет собой камеру в 3D-сцене
class Camera:
   def __init__(self, location, angle):
       self.location = location       # location - это точка в 3D-пространстве, где находится камера
       self.angle = angle       # angle - это угол, под которым камера смотрит на сцену

   # Метод rotate используется для вращения камеры
   def rotate(self, angle)-> None:
       pass

   # Метод move используется для перемещения камеры
   def move(self, point)-> None:
       pass


# Класс Scene представляет собой 3D-сцену
class Scene:
    # id - это уникальный идентификатор сцены
       # models - это список полигональных моделей, которые находятся на сцене
       # flashes - это список вспышек, которые находятся на сцене
    def init(self, id, models, flashes, cameras):
       self.ID = id
       if len(models) > 0:
           self.Models = models
       else:
           raise Exception("Должна быть одна модель")
       self.Flashes = flashes
       if len(cameras) > 0:
           self.cameras = cameras
       else:
           raise Exception("Должна быть одна камера")

   # Метод method1 - это пример метода, который может быть определен в классе Scene
   def method1(self, type1)->Type:
       pass

   # Метод method2 - это еще один пример метода, который может быть определен в классе Scene
   def method2(self, type1, type2)->Type:
       pass


# Класс Texture представляет собой текстуру
class Texture:
   pass


# Класс Poligon представляет собой полигон
class Poligon:
   def __init__(self, points):
       self.points = points       # points - это список точек, которые определяют полигон


# Класс PoligonalModel представляет собой полигональную модель
class PoligonalModel:
   # Метод __init__ инициализирует экземпляр класса
   def init(self, textures):
       self.poligons = []  # poligon - это полигон, который добавляется в список полигонов
       self.textures = textures  # textures - это список текстур, которые будут применены к полигонам
       self.poligons.append(Poligon(Point3D()))  # poligons - это список полигонов, которые составляют модель

