# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class EmpresaRuta(models.Model):
    personaMoral = models.ForeignKey('entidad.PersonaMoral')

    class Meta(object):
        verbose_name_plural = "Empresas Ruta"
        pass

    def __unicode__(self):
        return "%s, %s" % (self.id, self.personaMoral)
        pass

    pass


class Chofer(models.Model):

    miembroFisico = models.ForeignKey('entidad.MiembroFisico')

    class Meta(object):
        verbose_name_plural = "Choferes"
        pass

    def __unicode__(self):
        return "%s, %s" % (self.id, self.miembroFisico)
        pass

    pass


class Concecionario(models.Model):
    miembroFisico = models.ForeignKey('entidad.MiembroFisico')

    class Meta(object):
        verbose_name_plural = "Concecionarios"
        pass

    def __unicode__(self):
        return "%s, %s" % (self.id, self.miembroFisico)
        pass

    pass


class Administrador(models.Model):
    miembroFisico = models.ForeignKey('entidad.MiembroFisico')

    class Meta(object):
        verbose_name_plural = "Administradores"
        pass

    def __unicode__(self):
        return "%s, %s" % (self.id, self.miembroFisico)
        pass

    pass

class AdministradorMaster(models.Model):
    miembroFisico = models.ForeignKey('entidad.MiembroFisico')

    class Meta(object):
        verbose_name_plural = "Administradores Master"
        pass

    def __unicode__(self):
        return "%s, %s" % (self.id, self.miembroFisico)
        pass

    pass


class TipoLicenciaConducir(models.Model):
    clave = models.CharField(max_length=30, blank=True)
    nombre = models.CharField(max_length=100, blank=False)

    class Meta(object):
        verbose_name_plural = "Tipos de Licencia de Conducir"
        pass

    def __unicode__(self):
        return "%s, %s, %s" % (self.id, self.clave, self.nombre)
        pass

class LicenciaConducir(models.Model):

    clave = models.CharField(max_length=30, blank=True)
    chofer = models.ForeignKey(Chofer)
    tipoLicenciaConducir = models.ForeignKey(TipoLicenciaConducir)

    class Meta(object):
        verbose_name_plural = "Licencias de Conducir"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.id, self.clave, self.chofer, self.tipoLicenciaConducir)
        pass

    pass

