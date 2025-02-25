
class Person: # Clase padre
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self): # Método de saludo
        print("Hello! I am a person.")

class Student(Person): # Clase hija
    def __init__(self, name, age, student_id): # Constructor de la clase hija 
        super().__init__(name, age) # Llamamos al constructor de la clase padre con super() 
        self.student_id = student_id # Atributo de la clase hija

    def greet(self): # Método de saludo de la clase hija
        super().greet() # Llamamos al método de la clase padre con super()
        print(f"Hello, my student ID is {self.student_id}") # Mensaje de saludo de la clase hija

# Creamos una instancia de la clase Student
student = Student("Ana", 20, "S123")
student.greet()