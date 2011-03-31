from __future__ import division
from django.db import models

import re
import math

class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100)
  tags_relacionados = models.ManyToManyField('self')
  numero_busquedas=models.IntegerField(default=0)

  def IncrementarNumeroBusquedas(self):
      self.numero_busquedas+=1

  def __unicode__(self):
        return self.nombre

class TagsFactory(object):
  def GetTagsNamesFromString(self, tagsString):
      pattern=re.compile(' ')
      return pattern.split(tagsString)

  def GetIfExistOrBuildTag(self, name):
    try:
        tag=Tag.objects.get(nombre=name)
    except Tag.DoesNotExist:
        tag=Tag(nombre=name,numero_busquedas=0)
        tag.save()
    return tag

  def GetTagsFromString(self, param):
      tags=list()
      for name in self.GetTagsNamesFromString(param):
          tag = self.GetIfExistOrBuildTag(name)
          tags.append(tag)
      return tags

  def BuildTagsFromString(self, param):
    tags=self.GetTagsFromString(param)

    for tag in tags:
        for rel in set(tags)-set([tag]):
            tag.tags_relacionados.add(rel)
        tag.save()
    return tags

class HtmlFontSizer():
    html_size=['xx-small','x-small','small','medium','large','x-large','xx-large']

    def __init__(self,realMaxSize):
        self.max=realMaxSize

    def setSizeTo(self,obj,realSize):
        obj.size=self.html_size[self.calculateProporcionalValue(realSize)]

    def calculateProporcionalValue(self,tamanho):
        totalSizes=len(self.html_size)
        return min(int((tamanho*totalSizes)/self.max),totalSizes-1)
