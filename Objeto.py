class MODELO():
    def __init__(self,fecha,reportado,afectados,codigo):
        self.fecha=fecha
        self.reportado=reportado
        self.afectados=afectados
        self.codigo=codigo

class CANT_FECHA():
    def __init__(self,fecha,cantidad):
        self.fecha=fecha
        self.cantidad=cantidad

class CANT_REPORTADO():
    def __init__(self,usuario,cantidad):
        self.usuario=usuario
        self.cantidad=cantidad

class CANT_ERROR():
    def __init__(self,cod_error,cantidad):
        self.cod_error=cod_error
        self.cantidad=cantidad