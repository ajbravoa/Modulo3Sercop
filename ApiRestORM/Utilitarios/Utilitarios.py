class Mensajes:

    @staticmethod
    def CreacionOK():
        return "{Codigo:200, Mensaje: Registrado Correctamente}"

    @staticmethod
    def ActualizacionOK():
        return "{Codigo:200, Mensaje: Actualizado Correctamente}"

    @staticmethod
    def Error(self, mensaje):
        return "{Codigo:200, Mensaje: Actualizado Correctamente: " +  mensaje +"}"
