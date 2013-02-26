# -*- coding: utf-8 -*-


from localizacionbasica.models import Pais
from localizacionbasica.models import Estado
from localizacionbasica.models import Ciudad
from localizacionbasica.models import Colonia
from localizacionbasica.models import TipoDireccion
from localizacionbasica.models import Direccion

from django.contrib import admin

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Colonia)
admin.site.register(TipoDireccion)
admin.site.register(Direccion)