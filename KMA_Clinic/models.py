from django.db import models
from django.urls import reverse

# Create your models here.
#class KMA(models.Model):
	# def __init__(self, name ,address, birthdate, age, phone, husband):
	# 	super(KMA, self).__init__()
	# 	self.name      = models.CharField(max_length=100)
	# 	self.address   = models.CharField(blank= True, max_length=200)
	# 	self.birthdate = models.DateField('Birth_Date', blank=True, null=True)
	# 	self.age       = models.CharField(blank= True, max_length=100)
	# 	self.phone     = models.IntegerField(blank= True, default=0)
	# 	self.husband   = models.CharField(blank= True, max_length=100)
		
class KMA(models.Model):
	name      = models.CharField(max_length=100)
	address   = models.CharField(blank= True, max_length=200)
	birthdate = models.DateField('Birth Date', null=True)
	age       = models.CharField(blank= True, max_length=100)
	phone     = models.IntegerField(blank= True, default=0)
	husband   = models.CharField(blank= True, max_length=100)
	
	#age = age_

	def __str__(self):
		return self.name

	def get_url(self):
		return reverse('edit', kwargs={'id':self.id})

	def goto_home(self):
		return reverse('detail_id', kwargs={'id':self.id})

	def pass_age(self):
		return reverse("pass_age", kwargs={'age':self.age})

	# def age(self):
	# 	import datetime 	
	# 	return int((datetime.date.now() - self.birthdate).days / 365.25)
	# @property
	# def age_(self):
	# 	import datetime
	# 	dob = self.birthdate
	# 	tod = datetime.date.today()
	# 	my_age = (tod.year - dob.year) - float((tod.month, tod.day) < (dob.month, dob.day))
	# 	return my_age

	#age_cal = property(age_)

#	def save(self, *args, **kwargs):
#		self.age = self.age_()
#		super(KMA, self).save(*args, **kwargs)


class Visits(models.Model):
	patient_id = models.ForeignKey(KMA, on_delete=models.CASCADE)
	present_hist1 = models.CharField(blank= True, max_length=100)
	present_hist2 = models.CharField(blank= True, max_length=100)
	present_hist3 = models.CharField(blank= True, max_length=100)
	past_hist1 = models.CharField(blank= True, max_length=100)
	past_hist2 = models.CharField(blank= True, max_length=100)
	past_hist3 = models.CharField(blank= True, max_length=100)
	#patient_name = models.ForeignKey(KMA, on_delete=models.CASCADE)
	#kma = models.ForeignKey(KMA, on_delete=models.CASCADE)

	def __str__(self):
		return self.patient_id

	def url_visit(self):
		return reverse('visits_id', kwargs={'id':self.id})
		
