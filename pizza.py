"""
Задание создайте приложение онлайн закупки 
"""
class Terminal:
    '''
    Класс взайма действует с клиентом       
    '''
    def __init__(self):
        """
        Функция со списком заказов и списком топингов
        lis_order - Список заказа
        list_toping - Список топинга
        """
        self.list_order = []
        self.list_toping = []

    def main(self):
        """
        Функция отвечающий за взаймо действущее с клиентом
        и предлогает меню пиццы

        """
        if int(pizzeria_menu) == 1: 
            self.list_order+=["Peperoni"]
            Pizza.more_toping()
        if int(pizzeria_menu) == 3:
            self.list_order+=["SeaFood"]
            Pizza.more_toping()
        if int(pizzeria_menu) == 2:
            self.list_order += ["BBQpizza"]
            Pizza.more_toping()
        elif int(pizzeria_menu) == 0:
            print("Спасибо за покупку")
        else:
            print("Что-то пошло не так")
            
    def more_toping(self):
        """
        Функция взаймо действущее с клиентом и 
        предлогает топинг
        """
        extra_toping = input(" Хотите добавить дополнительные ингредиенты?\n (да/нет)")
        self.list_toping = []
        while True:
            if extra_toping.lower == "да":
                ferst_toping = input(" Выберите доп. ингредиент: \n Бекон \n Сыр \n Помидоры")
                second_toping = input(" Хотите добавить дополнительные ингредиенты?\n (да/нет)")
                self.list_toping.insert(ferst_toping)
                if second_toping.lower == "да":
                    continue
                else:
                    break
            else:
                break
        return self.list_toping


class Order:
    """
    Класс подверждающий оплату
    """
    def __init__(self):
        self.pizza = []

    def add_pizza(self, pizza):
        self.pizza.append(pizza)

    def calculate_total(self):
        total = 0
        for pizza in self.pizza:
            total += pizza.price
        return total



class Pizza:
    def __init__(self, dough, topping):
        self.dough = dough
        self.topping = topping
        self.price = 0

    def prepare(self):
        print("Готовим пиццу...")

    def bake(self):
        print("Выпекаем пиццу...")

    def cut(self):
        print("Нарезаем пиццу...")

    def pack(self):
        print("Упаковываем пиццу...")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__('тонкое', 'томатный', 'пепперони')
        self.price = 2000


class BarbecuePizza(Pizza):
    def __init__(self):
        super().__init__('толстое', 'барбекю', 'колбаса, лук, перец')
        self.price = 2500


class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__('обычное', 'сливочный', 'морепродукты')
        self.price = 3000

if __name__ == "__main__":

    fencing ="="*150
    print(" Какую пиццу хотите заказать?\n",fencing ," \n 1-Пицца Пепероний: Цена - 2500тг \n 2-Пицца Барбекю: Цена - 2000тг\n 3-Пицца Дары Моря: Цена - 3000\n (0-для завершение) \n",fencing)
    pizzeria_menu = input()
    Pizza.main(pizzeria_menu)

