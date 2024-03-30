class Human:
    default_name = 'Masha'
    default_age = 19

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name,)

    @staticmethod
    def default_info():
        print(Human.default_name)

    def __make_deal(self, house, price: int):
        self.__money -= price
        self.__house = house
    def earn_money(self, atemoney):
        self.__money +=atemoney
    def buy_house(self, house, discont):
        price = house.final_price(discont)
        if self.__money > price:
            print()
        else:
            print("предупреждение")
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def final_price(self,discont: int):
        return round(self._price * (100-discont)/100)

class SmallHouse(House):
    default_area = 40
    def _init_(self, price):
        super().__init__(SmallHouse.default_area,price)

Human.default_info()
human=Human()
House = SmallHouse(200)
Human.buy_house(House,20)










