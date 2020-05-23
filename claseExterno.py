import datetime

from claseEmpleado import Empleado

class Externo(Empleado):
    __fechaInicio : datetime.date
    __fechaFin : datetime.date
    __tarea = ''
    __montoViatico = 0
    __costoObra = 0
    __montoSeguroDeVida = 0

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin, tarea, montoViatico, costoDeObra, montoSeguroDeVida):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__tarea = tarea
        self.__montoViatico = montoViatico
        self.__costoObra = costoDeObra
        self.__montoSeguroDeVida = montoSeguroDeVida

    def __str__(self):
        s = Empleado.__str__(self)
        return s + '\nFecha de inicio: {}\nFecha de finalizacion: {}\nTarea: {}\nMonto viatico: {}\nCosto de la obra: {}' \
                   '\nMonto del seguro de vida: {}\nSueldo: {}'.format(self.__fechaInicio, self.__fechaFin, self.__tarea,
                                                                       self.__montoViatico, self.__costoObra,
                                                                       self.__montoSeguroDeVida, Empleado.sueldo(self))

    def getFechaInicio(self):
        return self.__fechaInicio
    def getFechaFin(self):
        return self.__fechaFin
    def getTarea(self):
        return self.__tarea
    def getMontoViatico(self):
        return self.__montoViatico
    def getCostoObra(self):
        return self.__costoObra
    def getMontoSeguroDeVida(self):
        return self.__montoSeguroDeVida
    def getSueldo(self):
        return float(self.getCostoObra() - self.getMontoViatico() - self.getMontoSeguroDeVida())
