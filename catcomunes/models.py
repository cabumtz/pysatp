# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.




class TipoTelefono(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s, %s" % (self.id, self.nombre)
        pass

    pass

class TipoMime(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s, %s" % (self.id, self.nombre, self.descripcion)
        pass

    pass

class TipoArchivo(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s, %s" % (self.id, self.nombre)
        pass

    pass