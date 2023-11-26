from abc import ABC, abstractmethod
from typing import List
from model_elements import *

# IModelChangeObserver - это абстрактный базовый класс (ABC), который определяет интерфейс для наблюдателей за изменениями в модели
class IModelChangeObserver(ABC):
   @abstractmethod
   def apply_update_model(self) -> None:
       pass

# IModelChanger - это абстрактный базовый класс (ABC), который определяет интерфейс для изменятелей модели
class IModelChanger(ABC):
   @abstractmethod
   def notify_change(self, sender) -> None:
       pass

# ModelStore - это класс, который реализует интерфейс IModelChanger
class ModelStore(IModelChanger):
   def __init__(self, changeObservers: List[IModelChangeObserver]):
       self.changeObservers = changeObservers
       self.models = PoligonalModel(textures, poligons)
       self.scenes = Scene(id, models, flashes)
       self.flashes = Flash(location, angle, color, power)
       self.cameras = Camera(location, angle)

       self.models = [self.model]
       self.scenes = [self.scene]
       self.flashes = [self.flash]
       self.cameras = [self.camera]

   def get_scene(self, id):
       for scene in self.scenes:
           if scene.id == id:
               return scene
       return None

   # Метод notify_change вызывает метод notify_change из суперкласса IModelChanger
   def notify_change(self, sender) -> None:
       super().notify_change(sender)
