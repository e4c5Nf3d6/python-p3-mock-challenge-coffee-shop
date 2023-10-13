class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception('name cannot be changed')
        elif isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception('name must be a string of at least 3 characters')
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if self.orders():
            return sum([order.price for order in self.orders()]) / len(self.orders())
        else:
            return 0

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('name must be a string between 1 and 15 characters')
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        most_money = 0
        aficionado = None
        for customer in list(set([order.customer for order in Order.all])):
            money_spent = sum([order.price for order in customer.orders() if order.coffee == coffee])
            if money_spent > most_money:
                most_money = money_spent
                aficionado = customer
        return aficionado
    
class Order:
    all =[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            raise Exception('price cannot be changed')
        elif isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise Exception('price must be a float between 1.0 and 10.0')
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception('customer must be an instance of the Customer class')
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception('coffee must be an instance of the Coffee class')    