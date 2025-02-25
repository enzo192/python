#concesionariodeautos
#puedes comprar un auto, venderlo, ver los autos en venta, ver los autos vendidos, ver los prcios de los autos

##------------------------clase consesionario------------------------

class Car:
    def __init__(self, brand, model, price, is_sold):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_sold = is_sold
        
    def sell(self):
        if self.is_sold:
            print("Car already sold.")
        else:
            self.is_sold = True
            print(f"{self.brand} {self.model} sold.")
            
    def buy(self):
        if self.is_sold:
            self.is_sold = False
            print(f"{self.brand} {self.model} bought.")
        else:
            print("Car already available.")
            
    def show_price(self):
        print(f"{self.brand} {self.model} price: {self.price}")
        
    def show_status(self):
        if self.is_sold:
            print(f"{self.brand} {self.model} is sold.")
        else:
            print(f"{self.brand} {self.model} is available.")
            

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.cars_bought = []
        
    def buy_car(self, car):
        if car.is_sold:
            print("Car is not available.")
        else:
            car.sell()
            self.cars_bought.append(car)
            
    def sell_car(self, car):
        if car in self.cars_bought:
            car.buy()
            self.cars_bought.remove(car)
        else:
            print("You have not bought this car.")
            
    def show_cars(self):
        print("Cars bought:")
        for car in self.cars_bought:
            print(f"{car.brand} {car.model}")
            

class CarDealer:
    def __init__(self):
        self.cars = []
        self.users = []
        
    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} added to inventory.")
        
    def add_user(self, user):
        self.users.append(user)
        print(f"{user.name} added to users.")
        
    def show_cars(self):
        print("Cars in inventory:")
        for car in self.cars:
            car.show_status()
            
    def show_sold_cars(self):
        print("Sold cars:")
        for car in self.cars:
            if car.is_sold:
                print(f"{car.brand} {car.model}")
                
    def show_prices(self):
        print("Prices:")
        for car in self.cars:
            car.show_price()
            

#crear instancia de carros
car1 = Car('KIA', 'Rio', 20000, False)
car2 = Car('Toyota', 'Corolla', 25000, False)
car3 = Car('Ferrari','Enzo',3600000,False)
car4 = Car('Chevrolet','Camaro',99990,False)
car5 = Car('Lamborghini','Huracan', 4000000, False)

#crear usuarios
user1 = User('Juan', 1)
user2 = User('Maria', 2)


#crear consesionario
cardealer = CarDealer()
cardealer.add_car(car1)
cardealer.add_car(car2)
cardealer.add_car(car3)
cardealer.add_car(car4)
cardealer.add_car(car5)

#mostrar carros
cardealer.show_cars()

#mostrar precios
cardealer.show_prices()

#comprar carros
user1.buy_car(car1)
user2.buy_car(car2)


#mostrar carros vendidos
cardealer.show_sold_cars()

#vender carros
user1.sell_car(car1)

#mostrar carros
cardealer.show_cars()




