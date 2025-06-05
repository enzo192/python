class Employee: 
    name: str
    age: int
    salary: float
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
        
    def introduce(self) -> str:
        return f"Hola, soy {self.name}, tengo {self.age} años y mi salario es {self.salary}."
    
employee1 = Employee("Juan", 30, 50000.0)
print(employee1.introduce())

