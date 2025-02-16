
class Vehicle:
    """
    Базовый класс для всех ТС.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация ТС.

        :param brand: Бренд ТС.
        :param model: Модель ТС.
        :param year: Год выпуска ТС.
        """
        self._brand = brand  # Непубличный атрибут, чтобы избежать прямого доступа к данным
        self._model = model  # Непубличный атрибут, чтобы избежать прямого доступа к данным
        self._year = year    # Непубличный атрибут, чтобы избежать прямого доступа к данным

    def __str__(self) -> str:
        """
        Возвращает строковое представление ТС.
        """
        return f"{self._year} {self._brand} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление ТС.
        """
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self._year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель ТС.

        :return: Сообщение о том, что двигатель запущен.
        """
        return f"{self._brand} {self._model} engine started."


class Car(Vehicle):
    """
    Класс легкового автомобиля, наследует от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Бренд легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self._doors = doors  # Непубличный атрибут, чтобы избежать прямого доступа к данным

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.
        """
        return f"{super().__str__()} with {self._doors} doors"

    def drive(self) -> str:
        """
        Перегруженный метод, который описывает, как легковой автомобиль движется.

        :return: Сообщение о том, что легковой автомобиль движется.
        """
        return f"{self._brand} {self._model} is driving smoothly."


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследует от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: Бренд грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность в тоннах.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self._capacity = capacity  # Непубличный атрибут, чтобы избежать прямого доступа к данным

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.
        """
        return f"{super().__str__()} with a capacity of {self._capacity} tons"

    def load(self, weight: float) -> str:
        """
        Метод для загрузки груза в грузовой автомобиль.

        :param weight: Вес груза в тоннах.
        :return: Сообщение о загрузке.
        :raises ValueError: Если вес груза превышает грузоподъемность.
        """
        if weight > self._capacity:
            raise ValueError(f"Cannot load {weight} tons. Maximum capacity is {self._capacity} tons.")
        return f"{weight} tons loaded in {self._brand} {self._model}."


if __name__ == "__main__":
    # Пример использования классов
    car = Car("Toyota", "Camry", 2022, 4)
    print(car)  # Вывод: 2022 Toyota Camry with 4 doors
    print(car.start_engine())  # Вывод: Toyota Camry engine started.
    print(car.drive())  # Вывод: Toyota Camry is driving smoothly.

    truck = Truck("Volvo", "FH16", 2020, 18)
    print(truck)  # Вывод: 2020 Volvo FH16 with a capacity of 18 tons
    print(truck.start_engine())  # Вывод: Volvo FH16 engine started.
    print(truck.load(15))  # Вывод: 15 tons loaded in Volvo FH16.
    # print(truck.load(20))  # Вывод: ValueError: Cannot load 20 tons. Maximum capacity is 18 tons.