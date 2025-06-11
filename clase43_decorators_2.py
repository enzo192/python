# Definimos un decorador para verificar el acceso
def check_access(func):
    def wrapper(employee):
        # Comprobar si el empleado tiene rol 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            # Si no es admin, mostrar mensaje de acceso denegado
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper

# Aplicamos el decorador a la función delete_employee
@check_access
def delete_employee(employee):
    # Imprime un mensaje indicando que el empleado ha sido eliminado
    print(f'El empleado {employee["name"]} ha sido eliminado.')

# Creamos un diccionario para un usuario admin
admin = {'name': 'Carlos', 'role': 'admin'}
# Creamos un diccionario para un usuario empleado
employee = {'name': 'Ana', 'role': 'employee'}

# Llamada a la función con un empleado (no admin)
#delete_employee(admin)
delete_employee(admin)

#implementa un decorador llamado log_employee_action que registre las acciones de los empleados en un archivo de texto.
def log_employee_action(func):
    def wrapper(employee):
        # Llamar a la función original
        result = func(employee)
        # Registrar la acción en un archivo de texto
        with open('employee_actions.log', 'a') as file:
            file.write(f'Empleado {employee["name"]} ha realizado una acción.\n')
        return result
    return wrapper

# Caso de uso: aplicar el decorador a una función
@log_employee_action
def view_profile(employee):
    print(f'Perfil de {employee["name"]}: rol {employee["role"]}')

# Ejemplo de uso
view_profile(admin)
view_profile(employee)