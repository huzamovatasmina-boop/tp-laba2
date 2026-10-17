from abc import ABC, abstractmethod


class GameObject:
    def __init__(self, object_id: int, name: str, x: int, y: int):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getX(self) -> int:
        return self._x

    def getY(self) -> int:
        return self._y
    

class Unit(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int, hp: float):
        super().__init__(object_id, name, x, y)
        self._hp = hp
        self._alive = True

    def getHp(self) -> float:
        return self._hp

    def isAlive(self) -> bool:
        return self._alive

    def receiveDamage(self, damage: float) -> None:
        self._hp -= damage

        if self._hp <= 0:
            self._alive = False


class Building(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int):
        super().__init__(object_id, name, x, y)
        self._built = False

    def isBuilt(self) -> bool:
        return self._built

    def setBuilt(self, built: bool) -> None:
        self._built = built


class Attacker(ABC):
    @abstractmethod
    def attack(self, target: Unit) -> None:
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass


class Fort(Building, Attacker):
    def attack(self, target: Unit) -> None:
        target.receiveDamage(30)


class MobileHouse(Building, Moveable):
    def move(self, x: int, y: int) -> None:
        self._x = x
        self._y = y


class Archer(Unit, Attacker, Moveable):
    def attack(self, target: Unit) -> None:
        target.receiveDamage(15)

    def move(self, x: int, y: int) -> None:
        self._x = x
        self._y = y


if __name__ == "__main__":
    archer = Archer(1, "Лучник", 0, 0, 100)
    enemy = Unit(2, "Противник", 4, 5, 50)
    fort = Fort(3, "Крепость", 10, 10)
    house = MobileHouse(4, "Дом на колёсах", 2, 3)

    archer.attack(enemy)
    print("После атаки лучника:", enemy.getHp())

    fort.attack(enemy)
    print("После атаки крепости:", enemy.getHp())

    archer.move(6, 7)
    house.move(12, 15)

    print("Позиция лучника:", archer.getX(), archer.getY())
    print("Позиция дома:", house.getX(), house.getY())
