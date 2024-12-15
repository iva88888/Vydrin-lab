
from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, material: str, weight: float):
        """
        Инициализация класса Furniture.

        :param material: Материал, из которого изготовлена мебель. Не должен быть пустым.
        :param weight: Вес мебели в килограммах. Должен быть положительным числом.

        :raises ValueError: Если material пустой или weight не положительный.

        >>> chair = Furniture("Wood", 5.0)
        >>> chair.material
        'Wood'
        >>> chair.weight
        5.0
        """
        if not material:
            raise ValueError("Material cannot be empty.")
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        self.material = material
        self.weight = weight

    @abstractmethod
    def assemble(self) -> None:
        """Собрать мебель."""
        ...

    @abstractmethod
    def disassemble(self) -> None:
        """Разобрать мебель."""
        ...


class Tree(ABC):
    def __init__(self, species: str, height: float):
        """
        Инициализация класса Tree.

        :param species: Вид дерева. Не должен быть пустым.
        :param height: Высота дерева в метрах. Должна быть положительным числом.

        :raises ValueError: Если species пустой или height не положительный.

        >>> pine = Tree("Pine", 20.0)
        >>> pine.species
        'Pine'
        >>> pine.height
        25.0
        """
        if not species:
            raise ValueError("Species cannot be empty.")
        if height <= 0:
            raise ValueError("Height must be a positive number.")

        self.species = species
        self.height = height

    @abstractmethod
    def grow(self, amount: float) -> None:
        """Увеличить высоту дерева на заданное количество метров."""
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """Сбросить листья дерева."""
        ...


class SocialMedia(ABC):
    def __init__(self, name: str, users: int):
        """
        Инициализация класса SocialMedia.

        :param name: Название социальной сети. Не должен быть пустым.
        :param users: Количество пользователей. Должно быть неотрицательным числом.

        :raises ValueError: Если name пустой или users отрицательный.

        >>> ok = SocialMedia("OK", 2900000000)
        >>> ok.name
        'OK'
        >>> ok.users
        3900000
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if users < 0:
            raise ValueError("Users cannot be negative.")

        self.name = name
        self.users = users

    @abstractmethod
    def post_update(self, content: str) -> None:
        """Опубликовать обновление с заданным содержимым."""
        ...

    @abstractmethod
    def delete_account(self) -> None:
        """Удалить аккаунт социальной сети."""
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
