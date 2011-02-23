from django.db import models

class Tag(models.Model):
  tag = models.CharField(max_length=100)
  tags = models.ManyToManyField('self')

  def __unicode__(self):
        return self.tag