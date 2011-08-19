from django.db import models
from posts.models import Post

class Dish(models.Model):
	name = models.CharField(max_length=20)
	price = models.FloatField()

class Menu(models.Model):
	dishes = models.ManyToManyField(Dish)

class Shop(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=3)
	zipcode = models.CharField(max_length=10)
	phone = models.CharField(max_length=30)
	description = models.TextField(max_length=200)
	thumbnail = models.ImageField(upload_to="static/Restaurant/thumbnail")
	posts = models.ManyToManyField(Post, blank=True, null=True)
	def __unicode__(self):
		return '%s' % (self.name)
	
class Restaurant(Shop):
	menu = models.ForeignKey(Menu)
	
class CoffeeShop(Shop):
	menu = models.ForeignKey(Menu)
	has_wifi = models.NullBooleanField()