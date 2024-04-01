# Interface for Pizza
class Pizza:
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

# Concrete classes for different types of pizzas
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing cheese pizza")

    def bake(self):
        print("Baking cheese pizza")

    def cut(self):
        print("Cutting cheese pizza")

class VeggiePizza(Pizza):
    def prepare(self):
        print("Preparing veggie pizza")

    def bake(self):
        print("Baking veggie pizza")

    def cut(self):
        print("Cutting veggie pizza")

# Factory class
class PizzaFactory:

    @staticmethod
    def get_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "veggie":
            return VeggiePizza()
        else:
            print("Invalid pizza type")
            return None

# Client code
pizza_factory = PizzaFactory()

cheese_pizza = pizza_factory.get_pizza("cheese")
cheese_pizza.prepare()
cheese_pizza.bake()
cheese_pizza.cut()

veggie_pizza = pizza_factory.get_pizza("veggie")
veggie_pizza.prepare()
veggie_pizza.bake()
veggie_pizza.cut()
