from claseEmpleado import Empleado

class DePlanta(Empleado):
    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self, dni, nombre, direccion, telefono, sueldoBasico, antiguedad):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def __str__(self):
        s = Empleado.__str__(self)
        return s + '\nSueldo basico: {}\nAntiguedad: {}\nSueldo: {}'\
            .format(self.__sueldoBasico, self.__antiguedad, Empleado.sueldo(self))

    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def getSueldo(self):
        return float(self.__sueldoBasico + (1/100)*self.__sueldoBasico*self.__antiguedad)
