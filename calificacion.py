from receta import Receta
from chef import Chef
from languageEN import EN

class Calificacion:
    
    ListCalificaciones = {}
    auto_increment_code = 0

    def __init__(
            self, usuario, rating, 
            description, para, code = None):
        '''ATTRIBUTES
            self._usuario
            self._rating
            self.description
            self._receta
            self._chef
        '''
        self.set_code(code)
        self.set_usuario(usuario)
        self.set_rating(puntaje)
        self.set_descripcion(descripcion)
        self._set_para(para)
        Calificacion.ListCalificaciones[self.get_code()] = self

    def set_code(self, code):
        aux_code = Receta.auto_increment_code
        if code:
            if code > aux_code:
                Receta.auto_increment_code = code
        else:
            Receta.auto_increment_code += 1
            code = Receta.auto_increment_code
        self._code = str(code)

    def get_code(self):
        return self._code

    def set_usuario(
            self, usuario):
        self._usuario = usuario

    def get_usuario(self):
        return self._usuario

    def set_rating(self, rating):
        self._rating = rating

    def get_rating(self):
        return self._rating

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def set_receta(
            self, receta):
        self._receta = receta
        receta.set_calificaciones(self)

    def get_receta(self):
        return self._receta

    def set_chef(
            self, chef):
        self._chef = chef
        chef.set_calificaciones(self)

    def get_chef(self):
        return self._chef

    def _set_para(para):
        if para.isInstance(Receta):
            self.set_receta(para)
            
        else:
            self.set_chef(para)
            