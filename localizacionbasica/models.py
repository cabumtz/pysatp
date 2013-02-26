# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Pais(models.Model):
    countrycode = models.IntegerField(null=True, blank=True)
    clave = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, blank=True)

    class Meta(object):
        verbose_name_plural = "Paises"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s, %s" % (self.id, self.countrycode, self.clave, self.nombre, self.abreviatura)
        pass

    pass

class Estado(models.Model):
    clave = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, blank=True)
    pais = models.ForeignKey(Pais)

    class Meta(object):
        verbose_name_plural = "Estados"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s, %s" % (self.id, self.clave, self.nombre, self.abreviatura, self.pais)
        pass

    pass

class Ciudad(models.Model):
    clave = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, blank=True)
    estado = models.ForeignKey(Estado)

    class Meta(object):
        verbose_name_plural = "Ciudades"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s, %s" % (self.id, self.clave, self.nombre, self.abreviatura, self.estado)
        pass

    pass

class Colonia(models.Model):
    clave = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad)

    class Meta(object):
        verbose_name_plural = "Colonias"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.id, self.clave, self.nombre, self.ciudad)
        pass

    pass

class TipoDireccion(models.Model):
    clave = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=50)
    comentario = models.TextField(max_length=300, blank=True)

    class Meta(object):
        verbose_name_plural = "Tipos de Dirección"
        pass

    def __unicode__(self):
        return "%s, %s, %s" % (self.id, self.clave, self.nombre)
        pass

    pass

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numeroExterior = models.CharField(max_length=20, blank=True)
    numeroInterior = models.CharField(max_length=20, blank=True)
    codigoPostal = models.CharField(max_length=20)
    ciudadDelegacionMunicipio = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    comentario = models.TextField(max_length=300, blank=True)

    estado = models.ForeignKey(Estado)
    tipoDireccion = models.ForeignKey(TipoDireccion)

    class Meta(object):
        verbose_name_plural = "Direcciones"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.calle, self.numeroExterior, self.numeroInterior,
            self.codigoPostal, self.ciudadDelegacionMunicipio, self.colonia, self.comentario, self.estado, self.tipoDireccion )
        pass

    pass

