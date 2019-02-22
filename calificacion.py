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
        self.set_rating(rating)
        self.set_description(description)
        self._set_para(para)
        Calificacion.ListCalificaciones[self.get_code()] = self
        archive = open('Calificacion_data.txt', 'a+')
        aux = None
        if isinstance(para, Receta):
            aux = para.get_code()
        else:
            aux = para.get_email()
        Str = usuario.get_email() +','+ rating + ','+ description +','+ aux +','+ self.get_code() +'\n'
        write = True
        archive.seek(0)
        for item in archive.readlines():
            if item.strip() == Str.strip():
                write = False
        if write:
            archive.write(Str)
        archive.close()
    def set_code(self, code):
        aux_code = Calificacion.auto_increment_code
        if code:
            if code > aux_code:
                Calificacion.auto_increment_code = code
        else:
            Calificacion.auto_increment_code += 1
            code = Calificacion.auto_increment_code
        self._code = str(code)

    def get_code(self):
        return self._code

    def set_usuario(
            self, usuario):
        self._usuario = usuario

    def get_usuario(self):
        return self._usuario

    def set_rating(self, rating):
        self._rating = int(rating)

    def get_rating(self):
        return self._rating

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def set_receta(self, receta):
        self._receta = receta
        if receta:
            receta.set_calificaciones(self)

    def get_receta(self):
        return self._receta

    def set_chef(self, chef):
        self._chef = chef
        if chef:
            chef.set_calificaciones(self)

    def get_chef(self):
        return self._chef

    def _set_para(self, para):
        if isinstance(para, Receta):
            self.set_receta(para)
            self.set_chef(None)
        else:
            self.set_chef(para)
            self.set_receta(None)

    def delete(self):
        code = self.get_Code()
        self.get_usuario().get_calificaciones().pop(code)
        if self.get_chef():
            self.get_chef().get_calificaciones_chef().pop(code)
        else:
            self.get_receta().get_calificaciones().pop(code)
        Calificacion.ListCalificaciones.pop(code)

    def __str__(self):
        code = self.get_code().zfill(6)
        para = self.get_chef()
        if para:
            para = self.get_chef().get_name()
        else:
            para = self.get_receta().get_name()
    
        rating = self.get_rating()
        description = self.get_description()
        Str = EN.men.get('calificacion_pattern') % (
                code, para, rating, description)
        return Str

    @staticmethod
    def see_my_calificacion(user):
        Str = EN.men.get('str_see_calificacion_header')
        for calificacion in Calificacion.ListCalificaciones.values():
            code = calificacion.get_code().zfill(6)
            para = calificacion.get_chef()
            if para:
                para = calificacion.get_chef().get_name()
            else:
                para = calificacion.get_receta().get_name()
        
            user = calificacion.get_usuario().get_name()
            rating = calificacion.get_rating()
            Str += EN.men.get('str_see_calificacion') % (
                    code, para, user, rating)
        return Str

    @staticmethod
    def see_calificacion():
        Str = EN.men.get('str_see_my_calificacion_header')
        for calificacion in Calificacion.ListCalificaciones.values():
            code = calificacion.get_code().zfill(6)
            para = calificacion.get_chef()
            if para:
                para = calificacion.get_chef().get_name()
            else:
                para = calificacion.get_receta().get_name()
        
            rating = calificacion.get_rating()
            Str += EN.men.get('str_see_my_calificacion') % (
                    code, para, rating)
        return Str

    @staticmethod
    def get_calificacion_by_code(code):
        return Calificacion.ListCalificaciones.get(code)

    @staticmethod
    def get_calificacion_by_code_user(user,code):
        return user.get_calificaciones().get(code)
        
    @staticmethod
    def best_chef():
        chefs = Chef.ListChefs
        best = None
        num = -1
        for chef in chefs.values():
            average = Calificacion.get_average_rating(chef)
            if average > num:
                num = average
                best = chef
        return best

    @staticmethod
    def get_average_rating(para):
        sum = 0
        for rating in para.get_calificaciones().values():
            sum += rating.get_rating()
        if len(para.get_calificaciones()) == 0:
            return 0
        else:
            return sum/len(para.get_calificaciones())
        
    @staticmethod
    def best_recetas():
        receta = Receta.ListRecetas
        best = None
        num = -1
        for receta in receta.values():
            average = Calificacion.get_average_rating(receta)
            if average > num:
                num = average
                best = receta
        return best