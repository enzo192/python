# herencia en concecionario de autos

class Vehicle: #creo la clase vehiculo
    def __init__(self, brand, model, price): #todas las clases hijas van a heredar todos los parametros de la clase padre vehiculo
        #Encapsulación: hace referencia a la protección de los datos de un objeto, para que estos no puedan ser modificados directamente
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self): #metodo para vender un vehiculo
        if self.is_available: #si el vehiculo esta disponible
            self.is_available = False #se cambia el estado a no disponible
            print(f"El vehiculo {self.brand}. Ha sido vendido") #se imprime que el vehiculo ha sido vendido
        else: #si no esta disponible
            print(f"El vehiculo {self.brand}. No está disponible") #se imprime que el vehiculo no esta disponible
    
    #Abstracción: es el proceso de ocultar los detalles de implementación y mostrar solo la funcionalidad al usuario
    def check_available(self): #metodo para verificar si un vehiculo esta disponible
        return self.is_available
    
    #Abstracción
    def get_price(self): #metodo para obtener el precio de un vehiculo
        return self.price
    
    def start_engine(self): #metodo para arrancar el motor
        raise NotImplementedError("Este metodo debe ser implementado por la subclase") #se lanza una excepcion si no se implementa el metodo
    
    def stop_engine(self): #metodo para detener el motor
        raise NotImplementedError("Este metodo debe ser implementado por la subclase") #se lanza una excepcion si no se implementa el metodo

#Herencia: es un mecanismo que permite que una clase herede atributos y métodos de otra clase
class Car(Vehicle): #creo la clase Car que hereda de la clase Vehicle
    #Polimorfismo: es la capacidad de un objeto para tomar diferentes formas
    def start_engine(self): 
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"
    
    #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} No está disponible"

#Herencia
class Bike(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"

     #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} No está disponible"

#Herencia
class Truck(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
    
    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} No está disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle): #metodo para comprar un vehiculo
        if vehicle.check_available(): #si el vehiculo esta disponible, se vende y se agrega a la lista de vehiculos comprados
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento,{vehicle.brand} no está disponible") 

    def inquire_vehicle(self, vehicle: Vehicle): #consulta si un vehiculo esta disponible y cuanto cuesta
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}")

class Dealership: #creo la clase Dealership
    def __init__(self): #inicializo la clase
        self.inventory = [] #tiene un inventario de vehiculos
        self.customers = [] #tiene una lista de clientes

    def add_vehicles(self, vehicle: Vehicle): #agrega un vehiculo al inventario
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer): #registra un cliente
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self): #muestra los vehiculos disponibles
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory: #recorre el inventario 
            if vehicle.check_available():   #si el vehiculo esta disponible
                print(f"- {vehicle.brand} por {vehicle.get_price()}") #se imprime el vehiculo y su precio

#instancias
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()