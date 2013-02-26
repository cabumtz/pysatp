# -*- coding: utf-8 -*-


from entidad.models import Entidad
from entidad.models import Sexo
from entidad.models import PersonaFisica
from entidad.models import TipoPersonaMoral
from entidad.models import PersonaMoral
from entidad.models import MiembroFisico

from django.contrib import admin

admin.site.register(Entidad)
admin.site.register(Sexo)
admin.site.register(PersonaFisica)
admin.site.register(TipoPersonaMoral)
admin.site.register(PersonaMoral)
admin.site.register(MiembroFisico)