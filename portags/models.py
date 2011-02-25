from django.db import models

class Tag(models.Model):
  nombre = models.CharField(max_length=100)
  tags_relacionados = models.ManyToManyField('self')
  numero_busquedas=models.IntegerField()
      
  def __unicode__(self):
        return self.tag