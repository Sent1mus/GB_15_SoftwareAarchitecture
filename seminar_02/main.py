from abc import ABC, abstractmethod
from random import choices


# Абстрактный класс для предметов игры
class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


# Абстрактный класс для фабрики предметов игры
class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


# Классы для различных типов наград
class Copper(IGameItem):
    def open(self):
        print('Copper!')


class Silver(IGameItem):
    def open(self):
        print('Silver!')


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Diamond(IGameItem):
    def open(self):
        print('Diamond!')


class Topaz(IGameItem):
    def open(self):
        print('Topaz!')


class Sapphire(IGameItem):
    def open(self):
        print('Sapphire!')


class Emerald(IGameItem):
    def open(self):
        print('Emerald!')


class Ruby(IGameItem):
    def open(self):
        print('Ruby!')


# Классы для создания различных типов наград
class CopperGenerator(ItemFabric):
    def create_item(self):
        return Copper()

    probability = 0.3


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()

    probability = 0.2


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()

    probability = 0.15


class DiamondGenerator(ItemFabric):
    def create_item(self):
        return Diamond()

    probability = 0.05


class TopazGenerator(ItemFabric):
    def create_item(self):
        return Topaz()

    probability = 0.05


class SapphireGenerator(ItemFabric):
    def create_item(self):
        return Sapphire()

    probability = 0.05


class EmeraldGenerator(ItemFabric):
    def create_item(self):
        return Emerald()

    probability = 0.05


class RubyGenerator(ItemFabric):
    def create_item(self):
        return Ruby()

    probability = 0.05


if __name__ == '__main__':
    # Список всех возможных наград
    reward_generators = [CopperGenerator(), SilverGenerator(), GoldGenerator(), DiamondGenerator(),
                         TopazGenerator(), SapphireGenerator(), EmeraldGenerator(), RubyGenerator()]

    # Создание и открытие случайной награды
    # Запускаем цикл 20 раз
    for i in range(20):
        # Выбираем генератор наград с учетом вероятностей выпадения каждой награды(probability).
        # Функция choices выбирает один элемент (k=1) из списка reward_generators с учетом вероятностей,
        # указанных в списке weights.
        # В этом случае weights создается как список вероятностей,
        # полученный из атрибута probability каждого генератора наград в списке reward_generators.
        # В результате получаем список с одним элементом - выбранным генератором наград.
        # Поскольку нам нужен сам генератор, а не список, мы используем индекс [0] для получения первого элемента.
        generator = choices(reward_generators, k=1, weights=[g.probability for g in reward_generators])[0]
        generator.create_item().open()