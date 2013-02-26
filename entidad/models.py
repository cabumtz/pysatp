# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.

class Entidad(models.Model):
    rfc = models.CharField(max_length=70, blank=True)
    clave = models.CharField(max_length=50, blank=True)
    comentario = models.TextField(max_length=300, blank=True)

    class Meta(object):
        verbose_name_plural = "Entidades"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.id, self.rfc, self.clave, self.comentario)
        pass

    pass

class Sexo(models.Model):
    clave = models.CharField(max_length=10, blank=True)
    abreviatura = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=50)

    class Meta(object):
        verbose_name_plural = "Sexos"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.id, self.clave, self.abreviatura, self.nombre)
        pass

    pass


class PersonaFisica(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    numeroSeguroSocial = models.CharField(max_length=50, blank=True)
    curp = models.CharField(max_length=50, blank=True)
    entidad = models.ForeignKey(Entidad)
    sexo = models.ForeignKey(Sexo)

    class Meta(object):
        verbose_name_plural = "Personas Físicas"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.nombre,
            self.apellidoPaterno, self.apellidoMaterno, self.fechaNacimiento,
            self.numeroSeguroSocial, self.curp, self.entidad)
        pass

    pass

class TipoPersonaMoral(models.Model):
    clave = models.CharField(max_length=10, blank=True)
    abreviatura = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=50)

    class Meta(object):
        verbose_name_plural = "Tipos Persona Moral"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.id, self.clave, self.abreviatura, self.nombre)
        pass

    pass


class PersonaMoral(models.Model):
    razonSocial = models.CharField(max_length=300)
    nombreComercial = models.CharField(max_length=300)
    fechaCreacion = models.DateField(null=True, blank=True)
    entidad = models.ForeignKey(Entidad)
    tipoPersonaMoral = models.ForeignKey(TipoPersonaMoral)

    class Meta(object):
        verbose_name_plural = "Personas Morales"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s, %s" % (self.id, self.razonSocial, self.nombreComercial,
            self.fechaCreacion, self.entidad)
        pass

    pass

class MiembroFisico(models.Model):
    clave = models.CharField(max_length=50, blank=True)
    personaMoral = models.ForeignKey(PersonaMoral)
    personaFisica = models.ForeignKey(PersonaFisica)

    class Meta(object):
        verbose_name_plural = "Miembros Físicos"
        pass

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.id, self.clave, self.personaMoral, self.personaFisica)
        pass

    pass

