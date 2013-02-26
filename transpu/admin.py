# -*- coding: utf-8 -*-
from transpu.models import EmpresaRuta
from transpu.models import Chofer
from transpu.models import Concecionario
from transpu.models import Administrador
from transpu.models import AdministradorMaster
from transpu.models import TipoLicenciaConducir
from transpu.models import LicenciaConducir

from django.contrib import admin

admin.site.register(EmpresaRuta)
admin.site.register(Chofer)
admin.site.register(Concecionario)
admin.site.register(Administrador)
admin.site.register(AdministradorMaster)
admin.site.register(TipoLicenciaConducir)
admin.site.register(LicenciaConducir)