import datetime

from claseEmpleado import Empleado

class Contratado(Empleado):
    valorPorHora = 100
    __fechaInicio : datetime.date
    __fechaFin : datetime.date
    __cantidadHorasTrabajadas = 0

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin, cantHoras):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__cantidadHorasTrabajadas = cantHoras

    def __str__(self):
        s = Empleado.__str__(self)
        return s + '\nFecha de inicio: {}\nFecha de finalizacion: {}\nCantidad de horas Trabajadas: {}\nSueldo: {}'\
            .format(self.__fechaInicio, self.__fechaFin, self.__cantidadHorasTrabajadas,Empleado.sueldo(self))

    @classmethod
    def modificarValorPorHora(cls, valor):
        if type(valor) == int:
            cls.valorPorHora = valor
        else:
            print('Error: se esperaba un valor de tipo entero.')

    @classmethod
    def getValorPorHora(cls):
        return cls.valorPorHora
    def getFechaInicio(self):
        return self.__fechaInicio
    def getFechaFin(self):
        return self.__fechaFin
    def getCantidadHorasTrabajadas(self):
        return self.__cantidadHorasTrabajadas
    def getSueldo(self):
        return float(self.getCantidadHorasTrabajadas() * self.getValorPorHora())
    def sumarHoras(self, horas):
        self.__cantidadHorasTrabajadas += horas
