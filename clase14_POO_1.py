#codigo explicado concecionario de autos
class Car: #creo la clase car
    def __init__(self, brand, model, price): #recibe 3 parametros
        self.brand = brand #creo el atributo brand
        self.model = model #creo el atributo model
        self.price = price #creo el atributo price
        self.is_available = True #creo el atributo is_available y le asigno True, loq ue significa que el auto está disponible.

    def sell(self): 
        if self.is_available: #dependiendo del estado del auto, se imprimo si se vende o no
            self.is_available = False
            print(f"El coche {self.brand} {self.model} ha sido vendido.")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible.")

    def check_availability(self): #metodo que retorna si esta disponible o no
        return self.is_available

    def get_price(self): #metodo que retorna el precio - este metodo con el nombre GET es para devolver el valor que esta en una variable
        return self.price


class Customer:
    def __init__(self, name):
        self.name = name #creo el atributo name
        self.cars_purchased = [] #tiene una coleccion de autos comprados

    def buy_car(self, car): #metodo para comprar un carro
        if car.check_availability(): #si el carro esta disponible, se vende y se agrega a la lista de autos comprados
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Lo siento, {car.brand} {car.model} no está disponible.") #si no esta disponible, se imprime que no esta disponible

    def inquire_car(self, car): #consulta si un carro esta disponible y cuanto cuesta
        availability = "disponible" if car.check_availability() else "no disponible"
        print(f"El coche {car.brand} {car.model} está {availability} y cuesta {car.get_price()}.")


class Dealership:
    def __init__(self):
        self.inventory = [] #tiene un inventario de autos
        self.customers = [] #tiene una lista de clientes

    def add_car(self, car): #agrega un carro al inventario
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido añadido al inventario.")

    def register_customer(self, customer): #registra un cliente
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la concesionaria.")

    def show_available_cars(self): #muestra los carros disponibles
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} por {car.get_price()}")


# Crear instancias de coches
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

# Crear instancia de cliente
customer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar coches y clientes
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)

# Mostrar coches disponibles
dealership.show_available_cars()

# Cliente consulta un coche
customer1.inquire_car(car1)

# Cliente compra un coche
customer1.buy_car(car1)

# Mostrar coches disponibles nuevamente
dealership.show_available_cars()

# Cliente intenta comprar un coche ya vendido
customer1.buy_car(car1)