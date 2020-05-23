import os
import datetime
from datetime import date
from datetime import datetime
from claseEmpleado import Empleado
from claseDePlanta import DePlanta
from claseContratado import Contratado
from claseExterno import Externo
from manejadorEmpleados import manejadorEmpleados
from claseMenu import Menu

def testEmpleados():
    empleadoDePlanta = DePlanta('123', 'Pepe Flores', 'Juan Jufre 838', '011222333', 55000, 10)
    print(empleadoDePlanta)
    print('')
    empleadoContratado = Contratado('456', 'Juan Gomez', 'Rivadavia 123', '011444555',
                                    date.today(), date.today() + datetime.timedelta(days=90), 20)
    print(empleadoContratado)
    print('')
    empleadoExterno = Externo('789', 'Elian Rodriguez', 'Rawson 251', '011668777',
                              date.today(), date.today() + datetime.timedelta(days=90), 'Carpinteria', 700, 15000, 2000)
    print(empleadoExterno)
if __name__ == '__main__':
    #testEmpleados()
    #fecha_str = "2020-05-22"
    #date_object = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    #print(date_object)

    dim = -1
    while dim < 1:
        dim = int(input('Ingrese la dimension del arreglo: '))
        os.system('cls')
        if dim < 1:
            print('Error: la dimension debe ser mayor a cero.')
    empleados = manejadorEmpleados(dim)
    empleados.cargarDatos()

    menu = Menu()
    salir = False
    while not salir:
        print('\n---------MENU---------\n0. Salir\n1. Registrar horas\n2. Total de tarea\n3. Ayuda\n4. Calcular sueldo')
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op, empleados)
        salir = op==0
