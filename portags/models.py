from django.db import models

class User(models.Model):
  email = models.EmailField()
  password = models.CharField(max_length=20) 

  def __unicode__(self):
        return self.email

class Tag(models.Model):
  tag = models.CharField(max_length=100)
  tags = models.ManyToManyField('self')
  user=models.ForeignKey(User)

  def __unicode__(self):
        return self.tag