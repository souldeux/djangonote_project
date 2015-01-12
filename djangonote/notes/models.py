from django.db import models

# Create your models here.

class Note(models.Model):
	label = models.CharField(max_length=200)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField('Tag', related_name='notes', blank=True)
	
	def __unicode__(self):
		return self.label
		

class Tag(models.Model):
	label = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	
	def __unicode__(self):
		return self.label