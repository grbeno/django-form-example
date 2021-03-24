from django.db import models

class Projectname(models.Model):
	project = models.CharField(max_length=20)

	def __str__(self):
		return self.project

class Modelform1(models.Model):
	ph = models.CharField(max_length=20) 
	thk = models.IntegerField()
	ka = models.IntegerField() 
	humusz = models.CharField(max_length=20)

class Modelform2(models.Model):
	p2o5 = models.CharField(max_length=20) 
	k2o = models.CharField(max_length=20)